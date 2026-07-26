# Solución razonada — Informe semanal de operaciones

## Contrato

- **Grano:** una fila por intento de cobro (`operacion_id`). Si el sistema permite reintentos, un cliente puede aparecer varias veces y no debe contarse como varios clientes.
- **Periodo:** `[inicio, fin)`: se incluye `inicio` y se excluye `fin`. Con semanas consecutivas no hay una hora duplicada en el cambio.
- **Cobrado:** solo `estado = 'pagada'`; la moneda debe ser EUR o convertirse antes de sumar.
- **Exclusión:** `es_prueba = 1`. El informe registra cuántas filas fueron excluidas.

## Extracción y controles

La consulta debe usar parámetros para las fechas y un usuario de solo lectura. Después de extraer, se validan las columnas, que no haya duplicados de `operacion_id`, que las fechas estén dentro del periodo, y que una fila pagada tenga importe no nulo y no negativo si ese es el contrato de negocio.

El total pagado se comprueba de dos maneras: suma del DataFrame de pagos y consulta SQL independiente `SUM(importe_eur)` sobre el mismo periodo y filtro. Dos cálculos no son totalmente independientes si copian la misma condición errónea; por eso el contrato de estados se revisa y el número de filas por estado queda visible.

## Estructura de entrega

`Resumen` contiene indicadores y desglose por canal. `Detalle` debe contener todos los intentos no de prueba si el consumidor necesita auditar el denominador; si se entrega solo pagos, debe llamarse `Detalle_pagados` y el resumen debe señalarlo. `Rechazados` incluye pendientes, devueltas, rechazadas y la regla usada. `Conciliacion` muestra control, valor, umbral, resultado y acción. `Metadatos` permite reproducir la semana y versión.

La tasa de pago no es pagos / filas de `Detalle` cuando `Detalle` ya está filtrado a pagos. Su denominador correcto sería intentos elegibles no de prueba, tras decidir si los pendientes pertenecen al periodo de intento o deben esperar a cierre. El control es publicar, junto a toda tasa, las filas del numerador, las del denominador y el filtro de cada una.

## Reparto de herramientas y privacidad

Power Query puede cargar y normalizar CSV recurrentes: tipos, separadores, nombres y anexado. SQL filtra y agrega cerca de la base; Python valida, registra y genera el libro; Excel permite revisión, tablas dinámicas y anotaciones de negocio. No se exportaría `cliente_email` al destinatario si no necesita contactar al cliente: es información personal que no aporta a la conciliación.

Una entrega no se envía si falla unicidad, periodo o conciliación. Se genera un registro de fallo con parámetros y conteos, sin datos sensibles, y se comunica la incidencia.

