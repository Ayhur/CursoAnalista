# Caso evaluable - Lumen Market: ingresos y conversión

## Contexto

Usa el esquema y los datos del [laboratorio SQL](../../../notebooks/practicas/09-lumen-market-sql.py). Dirección pide saber si el canal app convierte y factura mejor que web durante la primera semana de julio de 2026. No aceptes la pregunta sin contrato: decide y declara qué significa cada medida.

## Entregables

1. Escribe el grano, población, periodo `[2026-07-01, 2026-07-08)`, zona temporal asumida y exclusiones de tu análisis.
2. Con una CTE, calcula `importe_por_pedido` desde `lineas_pedido`; devuelve por `canal` pedidos pagados, clientes compradores únicos e ingresos. Explica por qué no sumas un supuesto total de `pedidos` tras unir líneas.
3. Escribe un anti-join que localice pedidos `pagado` sin un pago `liquidado`. ¿Es ingreso cero, dato faltante o una incidencia? Justifica sin inventar la regla.
4. Define el funnel por cliente y día: `view_product` -> `checkout_started` -> `purchase`, en ese orden. Explica por qué contar filas de `eventos` daría otra métrica. Propón un control de identidad, orden y duplicado.
5. Diseña, sin ejecutar, un documento MongoDB para el pedido y justifica embedding o referencia de líneas. Después, para DynamoDB, da un patrón de acceso, PK, SK y un GSI para una cola operativa. Indica una pregunta que llevarías a OLAP en vez de DynamoDB.

## Rúbrica

| Criterio | Evidencia esperada |
| --- | --- |
| Contrato | grano, periodo y población explícitos |
| SQL | CTE correcta, join que no multiplica ingresos, filtros claros |
| Calidad | anti-join y tratamiento prudente de ausencia |
| Funnel | entidad única, orden temporal y controles |
| Arquitectura | decisiones justificadas por acceso y no por moda |

Consulta la [solución razonada](../../../soluciones/temario-09/consulta-conversion.md) solo tras intentar el caso.
