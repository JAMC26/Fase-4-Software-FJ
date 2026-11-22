# Pruebas de la simulación

Inicio: 2026-11-22T12:05:04-05:00  
Fin: 2026-11-22T12:05:04-05:00  
Comando: python main.py  
Código de salida: 0

Se ejecutaron 20 operaciones. Se revisó que el registro incluyera una operación fallida y la última operación completada. Los errores controlados forman parte de la simulación.

También se comprobaron los costos de sala, equipo y asesoría; el rechazo de procesamiento sin confirmar; y la conservación del estado al rechazar un descuento inválido.

## Salida de la terminal

```text

1. Registrar cliente válido
Cliente: Ana Pérez (ID 1001)
Operación finalizada; la simulación continúa.

2. Rechazar cliente sin nombre
Error controlado: Nombre es obligatorio
Operación finalizada; la simulación continúa.

3. Rechazar identificación repetida
Error controlado: La identificación ya está registrada
Operación finalizada; la simulación continúa.

4. Registrar sala
Sala Reuniones: capacidad 12; tarifa $30,000.00/hora
Operación finalizada; la simulación continúa.

5. Registrar equipo
Equipo Proyector: tarifa $15,000.00/hora; mantenimiento $5,000.00
Operación finalizada; la simulación continúa.

6. Registrar asesoría
Asesoría Tecnológica: Software; tarifa $50,000.00/hora
Operación finalizada; la simulación continúa.

7. Rechazar tarifa no numérica
Error controlado: Tarifa debe ser un número válido
Operación finalizada; la simulación continúa.

8. Rechazar parámetro faltante
Error controlado: Equipo.__init__() missing 1 required positional argument: 'mantenimiento'
Operación finalizada; la simulación continúa.

9. Crear reserva válida
Ana Pérez | Sala Reuniones: capacidad 12; tarifa $30,000.00/hora | 2 h | pendiente
Operación finalizada; la simulación continúa.

10. Confirmar reserva
Ana Pérez | Sala Reuniones: capacidad 12; tarifa $30,000.00/hora | 2 h | confirmada
Operación finalizada; la simulación continúa.

11. Procesar con 19 % de impuesto y 10 % de descuento
Ana Pérez | Sala Reuniones: capacidad 12; tarifa $30,000.00/hora | 2 h | procesada | Total: $64,260.00
Operación finalizada; la simulación continúa.

12. Rechazar cancelación de reserva procesada
Error controlado: Solo se puede cancelar una reserva pendiente o confirmada
Operación finalizada; la simulación continúa.

13. Registrar sala no disponible
Sala Sala ocupada: capacidad 5; tarifa $20,000.00/hora
Operación finalizada; la simulación continúa.

14. Rechazar confirmación de servicio no disponible
Error controlado: El servicio no está disponible
Operación finalizada; la simulación continúa.

15. Rechazar duración cero
Error controlado: Duración debe ser finito y mayor o igual a 0.01
Operación finalizada; la simulación continúa.

16. Calcular precio de equipo
Total: $35,000.00
Operación finalizada; la simulación continúa.

17. Calcular precio de asesoría
Total: $100,000.00
Operación finalizada; la simulación continúa.

18. Rechazar descuento superior al 100 %
Error controlado: Los porcentajes no pueden superar el 100 %
Operación finalizada; la simulación continúa.

19. Confirmar y cancelar una reserva
Ana Pérez | Asesoría Tecnológica: Software; tarifa $50,000.00/hora | 1 h | cancelada
Operación finalizada; la simulación continúa.

20. Confirmar que el programa sigue activo
Clientes: 1; servicios: 4; reservas: 3
Operación finalizada; la simulación continúa.

```
