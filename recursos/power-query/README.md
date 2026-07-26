# Práctica guiada de Power Query — Norte Operaciones

Este material convierte la lección 16.3 en una práctica verificable. No necesitas ejecutar Python: abre Excel de escritorio, guarda estos CSV en una carpeta local y sigue [pasos-explicados.md](pasos-explicados.md).

## Material

- `operaciones-brutas.csv`: fuente semanal con separador `;`, coma decimal, una fila interna y estados que no deben confundirse.
- `clientes.csv`: referencia de clientes para practicar una combinación por clave.
- `consulta-operaciones.m`: consulta Power Query completa y comentada.
- `resultado-esperado.csv`: resultado después de tipar, filtrar pruebas, combinar y clasificar la exclusión del total.

El resultado esperado contiene cinco operaciones no internas: dos pagadas, una rechazada, una devuelta y una pendiente. El total pagado es **170,00 EUR**. No es un total de todos los intentos ni una tasa de pago.

