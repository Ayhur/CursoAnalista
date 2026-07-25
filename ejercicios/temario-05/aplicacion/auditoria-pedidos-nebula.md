# Auditoría de pedidos de Nébula

## Situación

Trabajas con [pedidos_nebula.csv](../../../datasets/pandas/pedidos_nebula.csv) y [clientes_nebula.csv](../../../datasets/pandas/clientes_nebula.csv). Dirección pide ingresos netos de pedidos pagados por canal para junio. Una fila pretende ser un pedido, pero la exportación contiene una actualización del mismo ID, una fecha inválida, un importe negativo, un canal no catalogado y un cliente sin ficha.

## Entrega

1. Escribe un contrato mínimo: grano, clave, estados incluidos, fórmula de ingresos netos, unidad y una limitación.
2. Carga el CSV sin asumir separador ni tipo de IDs. Muestra cinco comprobaciones de perfilado y explica qué decisión permite cada una.
3. Convierte fecha, importe y descuento. Clasifica las filas que no cumplan las reglas; no uses `dropna()` global.
4. Distingue el duplicado técnico de la actualización de `P-1002`. Justifica qué versión conservarías y qué evidencia necesitarías para aprobar esa regla.
5. Calcula `importe_neto`, resume pedidos distintos e ingresos netos por canal y reconcilia el total con el detalle.
6. Une los clientes con `how`, `validate` e `indicator` elegidos explícitamente. Indica cómo tratarías `left_only` en un informe de ingresos y en uno de segmentación.
7. Redacta un registro de linaje de cuatro líneas: fuente, transformaciones, controles y limitación. Ejecuta el [laboratorio](../../../notebooks/practicas/05-pipeline-pedidos-nebula.py) solo después de intentar tu solución.

No entregues solamente código: cada filtro y cada exclusión debe tener una razón de negocio o calidad.
