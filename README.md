# Software FJ: gestión de clientes, servicios y reservas

Proyecto para la Fase 4 del curso Programación (213023). Utiliza Python 3 y la biblioteca estándar, sin bases de datos ni paquetes externos.

## Ejecución

En una terminal abierta en esta carpeta, ejecute `python main.py` o `py main.py` en Windows. La simulación ejecuta 20 operaciones, incluyendo casos válidos y errores controlados. El archivo `eventos.log` se crea en el directorio de ejecución y registra los eventos; si no puede abrirse, se informa y se utiliza la consola.

`sistema.py` contiene las entidades, validaciones y manejo de errores. `main.py` ejecuta la simulación. Los clientes, servicios y reservas se mantienen en listas en memoria y no se recuperan al cerrar el programa.

## Supuestos

Las tarifas y los porcentajes son valores de ejemplo. El descuento se aplica antes del impuesto. La disponibilidad es un dato del servicio; el programa no gestiona fechas ni conflictos de horario. Una reserva pendiente puede confirmarse o cancelarse; una confirmada puede procesarse o cancelarse. Una operación inválida no cambia su estado.

Consulte `PRUEBAS.md` para ver la ejecución de la simulación y `PRUEBAS_ESCRITORIO.md` para comparar los resultados esperados y observados de cada caso.
