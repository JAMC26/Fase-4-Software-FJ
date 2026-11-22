# Pruebas de escritorio

Fecha de ejecución: 2026-11-22T12:14:23-05:00

Los resultados observados corresponden a la ejecución de los casos sobre el código de esta rama. Las tarifas son valores de ejemplo.

| Caso | Entrada | Resultado esperado | Resultado observado | Evaluación |
| --- | --- | --- | --- | --- |
| Cliente válido | ID 1001; Ana Pérez; ana@example.com | Ana Pérez | Ana Pérez | Cumple |
| Nombre vacío | nombre vacío | ErrorValidacion: Nombre es obligatorio | ErrorValidacion: Nombre es obligatorio | Cumple |
| Tarifa inválida | tarifa abc | ErrorValidacion: Tarifa debe ser un número válido | ErrorValidacion: Tarifa debe ser un número válido | Cumple |
| Costo de sala | 2 h; impuesto 19 %; descuento 10 % | 64260.0 | 64260.0 | Cumple |
| Costo de equipo | 2 h; tarifa 15000; mantenimiento 5000 | 35000.0 | 35000.0 | Cumple |
| Costo de asesoría | 2 h; tarifa 50000 | 100000.0 | 100000.0 | Cumple |
| Procesar sin confirmar | reserva pendiente | ErrorReserva: Solo se puede procesar una reserva confirmada | ErrorReserva: Solo se puede procesar una reserva confirmada | Cumple |
| Descuento inválido | reserva confirmada; descuento 101 % | ErrorValidacion: Los porcentajes no pueden superar el 100 % | ErrorValidacion: Los porcentajes no pueden superar el 100 % | Cumple |
| Estado tras error | descuento rechazado | confirmada | confirmada | Cumple |
| Cancelación | reserva confirmada | cancelada | cancelada | Cumple |
| Servicio no disponible | confirmar sala no disponible | ErrorReserva: El servicio no está disponible | ErrorReserva: El servicio no está disponible | Cumple |

Resultado: 11 de 11 casos cumplen.
