# Proyecto — Informe semanal de operaciones

## Situación

Cada lunes, Norte Operaciones necesita un libro Excel del periodo anterior. La tabla `operaciones` contiene una fila por **intento de cobro**. El negocio llama «cobrado» solo a los estados `pagada`; `devuelta` no es un pago y `pendiente` no debe mezclarse con un rechazo. Hay una marca `es_prueba` para filas internas.

El archivo debe permitir decidir si se puede comunicar el total semanal y, si no, por qué debe bloquearse.

## Entregable

Diseña —o completa a partir del laboratorio— un proceso que genere un `.xlsx` con estas hojas:

1. `Resumen`: total cobrado, intentos, operaciones pagadas y distribución por canal.
2. `Detalle`: operaciones del periodo, excluyendo pruebas, con filtros y encabezado congelado.
3. `Rechazados`: filas que no entran en el total pagado, con un motivo explícito.
4. `Conciliacion`: controles de filas, IDs únicos, nulos, rango de fechas y total pagado frente a cálculo independiente.
5. `Metadatos`: inicio, fin exclusivo, fecha UTC de generación, fuente, versión y estado final de controles.

## Requisitos de razonamiento

- Declara el contrato: grano, periodo, estados, exclusiones y moneda.
- Usa una consulta SQL parametrizada. Explica por qué `fin` es exclusivo.
- Propón una regla para bloquear el archivo si aparece un `operacion_id` duplicado o un importe pagado nulo.
- Explica qué parte harías con Power Query si los archivos llegan como CSV, qué parte con SQL/Python y qué parte dejarías para revisión en Excel.
- Indica qué dato no exportarías si `cliente_email` existiera y el destinatario fuese solo Operaciones.

## Prueba de auditoría

Un compañero calcula una tasa de pago de 100 % porque divide pagos entre filas de la hoja `Detalle`, pero esa hoja solo contiene pagos. Explica el error, corrige el denominador y añade un control que impida repetirlo.

Consulta la [solución razonada](../../soluciones/temario-16/informe-semanal-operaciones.md) solo después de intentar el diseño.

