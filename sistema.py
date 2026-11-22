"""Entidades iniciales para el sistema de reservas de Software FJ."""

from abc import ABC, abstractmethod
import logging
import math


class ErrorValidacion(Exception):
    """Indica que un dato obligatorio no es válido."""


class ErrorReserva(Exception):
    """Indica que una operación de reserva no está permitida."""


def validar_texto(valor, nombre):
    """Comprueba que el dato sea una cadena con contenido."""
    if not isinstance(valor, str) or not valor.strip():
        raise ErrorValidacion(f"{nombre} es obligatorio")
    return valor.strip()


class Entidad(ABC):
    """Define la operación común para describir una entidad."""

    @abstractmethod
    def describir(self):
        """Devuelve una descripción de la entidad."""


class Cliente(Entidad):
    """Representa un cliente con datos personales de solo lectura."""

    def __init__(self, identificacion, nombre, correo):
        self.__identificacion = validar_texto(identificacion, "Identificación")
        self.__nombre = validar_texto(nombre, "Nombre")
        correo = validar_texto(correo, "Correo")
        partes = correo.split("@")
        if len(partes) != 2 or any(not parte or " " in parte for parte in partes):
            raise ErrorValidacion("El correo debe incluir usuario y dominio")
        self.__correo = correo

    @property
    def identificacion(self):
        return self.__identificacion

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    def describir(self):
        return f"Cliente: {self.nombre} (ID {self.identificacion})"


def validar_numero(valor, nombre, minimo=0):
    """Convierte y valida un número, conservando la causa de conversión."""
    try:
        if isinstance(valor, bool):
            raise ValueError("Se requiere un número")
        resultado = float(valor)
    except (ValueError, TypeError, OverflowError) as error:
        raise ErrorValidacion(f"{nombre} debe ser un número válido") from error
    if not math.isfinite(resultado) or resultado < minimo:
        raise ErrorValidacion(f"{nombre} debe ser finito y mayor o igual a {minimo}")
    return resultado


class Servicio(Entidad, ABC):
    """Reúne los datos y operaciones comunes de los servicios."""

    def __init__(self, nombre, tarifa, disponible=True):
        self._nombre = validar_texto(nombre, "Nombre del servicio")
        self._tarifa = validar_numero(tarifa, "Tarifa", 0.01)
        if not isinstance(disponible, bool):
            raise ErrorValidacion("La disponibilidad debe ser verdadera o falsa")
        self._disponible = disponible

    @property
    def disponible(self):
        return self._disponible

    def validar_parametros(self, duracion):
        """Valida la duración expresada en horas."""
        return validar_numero(duracion, "Duración", 0.01)

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """Calcula el costo aplicando primero descuento y después impuesto."""
        horas = self.validar_parametros(duracion)
        impuesto = validar_numero(impuesto, "Impuesto")
        descuento = validar_numero(descuento, "Descuento")
        if impuesto > 100 or descuento > 100:
            raise ErrorValidacion("Los porcentajes no pueden superar el 100 %")
        total = self._costo_base(horas) * (1 - descuento / 100) * (1 + impuesto / 100)
        if not math.isfinite(total) or total < 0:
            raise ErrorValidacion("El costo calculado no es válido")
        return round(total, 2)

    @abstractmethod
    def _costo_base(self, horas):
        """Calcula el costo antes de impuestos y descuentos."""


class Sala(Servicio):
    """Servicio de sala cobrado por hora."""

    def __init__(self, nombre, tarifa, capacidad, disponible=True):
        super().__init__(nombre, tarifa, disponible)
        if isinstance(capacidad, bool) or not isinstance(capacidad, int) or capacidad < 1:
            raise ErrorValidacion("La capacidad debe ser un entero positivo")
        self._capacidad = capacidad

    def _costo_base(self, horas):
        return self._tarifa * horas

    def describir(self):
        return f"Sala {self._nombre}: capacidad {self._capacidad}; tarifa ${self._tarifa:,.2f}/hora"


class Equipo(Servicio):
    """Servicio de equipo con un cargo fijo de mantenimiento."""

    def __init__(self, nombre, tarifa, mantenimiento, disponible=True):
        super().__init__(nombre, tarifa, disponible)
        self._mantenimiento = validar_numero(mantenimiento, "Mantenimiento")

    def _costo_base(self, horas):
        return self._tarifa * horas + self._mantenimiento

    def describir(self):
        return f"Equipo {self._nombre}: tarifa ${self._tarifa:,.2f}/hora; mantenimiento ${self._mantenimiento:,.2f}"


class Asesoria(Servicio):
    """Servicio de asesoría por especialidad y por hora."""

    def __init__(self, nombre, tarifa, especialidad, disponible=True):
        super().__init__(nombre, tarifa, disponible)
        self._especialidad = validar_texto(especialidad, "Especialidad")

    def _costo_base(self, horas):
        return self._tarifa * horas

    def describir(self):
        return f"Asesoría {self._nombre}: {self._especialidad}; tarifa ${self._tarifa:,.2f}/hora"


class Reserva(Entidad):
    """Relaciona cliente y servicio y controla el estado de una reserva."""

    def __init__(self, cliente, servicio, duracion):
        if not isinstance(cliente, Cliente) or not isinstance(servicio, Servicio):
            raise ErrorValidacion("La reserva requiere un cliente y un servicio válidos")
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = servicio.validar_parametros(duracion)
        self._estado = "pendiente"

    @property
    def estado(self):
        return self._estado

    def confirmar(self):
        """Confirma una reserva pendiente si el servicio está disponible."""
        if self._estado != "pendiente":
            raise ErrorReserva("Solo se puede confirmar una reserva pendiente")
        if not self._servicio.disponible:
            raise ErrorReserva("El servicio no está disponible")
        self._estado = "confirmada"
        return self.describir()

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""
        if self._estado not in ("pendiente", "confirmada"):
            raise ErrorReserva("Solo se puede cancelar una reserva pendiente o confirmada")
        self._estado = "cancelada"
        return self.describir()

    def procesar(self, impuesto=0, descuento=0):
        """Calcula el costo de una reserva confirmada y la marca procesada."""
        if self._estado != "confirmada":
            raise ErrorReserva("Solo se puede procesar una reserva confirmada")
        costo = self._servicio.calcular_costo(self._duracion, impuesto, descuento)
        self._estado = "procesada"
        return f"{self.describir()} | Total: ${costo:,.2f}"

    def describir(self):
        return (f"{self._cliente.nombre} | {self._servicio.describir()} | "
                f"{self._duracion:g} h | {self._estado}")


class Sistema:
    """Mantiene clientes, servicios y reservas en listas durante la ejecución."""

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise ErrorValidacion("Cliente inválido")
        if any(item.identificacion == cliente.identificacion for item in self.clientes):
            raise ErrorValidacion("La identificación ya está registrada")
        self.clientes.append(cliente)
        return cliente.describir()

    def registrar_servicio(self, servicio):
        if not isinstance(servicio, Servicio):
            raise ErrorValidacion("Servicio inválido")
        self.servicios.append(servicio)
        return servicio.describir()

    def crear_reserva(self, cliente, servicio, duracion):
        if cliente not in self.clientes or servicio not in self.servicios:
            raise ErrorReserva("El cliente y el servicio deben estar registrados")
        reserva = Reserva(cliente, servicio, duracion)
        self.reservas.append(reserva)
        return reserva


def configurar_registro():
    """Configura el registro de eventos en el directorio de ejecución."""
    try:
        logging.basicConfig(filename="eventos.log", level=logging.INFO,
                            format="%(asctime)s | %(levelname)s | %(message)s",
                            encoding="utf-8")
    except OSError as error:
        print(f"No se pudo abrir eventos.log: {error}. Se utilizará la consola.")
        logging.basicConfig(level=logging.INFO)


def ejecutar_operacion(indice, descripcion, accion):
    """Registra el resultado de cada operación y continúa con la siguiente."""
    print(f"\n{indice}. {descripcion}")
    try:
        resultado = accion()
    except (ErrorValidacion, ErrorReserva, TypeError) as error:
        logging.exception("Operación %s fallida: %s", indice, descripcion)
        print(f"Error controlado: {error}")
    except Exception as error:
        logging.exception("Error inesperado en operación %s: %s", indice, descripcion)
        print(f"Error inesperado: {error}")
    else:
        logging.info("Operación %s completada: %s", indice, descripcion)
        if resultado is not None:
            print(resultado)
    finally:
        print("Operación finalizada; la simulación continúa.")
