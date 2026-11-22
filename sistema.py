"""Entidades iniciales para el sistema de reservas de Software FJ."""

from abc import ABC, abstractmethod


class ErrorValidacion(Exception):
    """Indica que un dato obligatorio no es válido."""


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
