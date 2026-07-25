# Práctica aplicada — Auditoría de Mercado Faro

## Entrega

Escribe una respuesta razonada. Antes de mirar la solución, puedes ejecutar el laboratorio del bloque, pero explica con tus propias palabras qué comprueba cada resultado.

## Contexto

La directora pide: «publicad mañana el número de pedidos pagados y su ingreso del 24 de julio por canal». Recibes [`pedidos.csv`](../../../datasets/temario-01/pedidos.csv) y [`lineas_pedido.csv`](../../../datasets/temario-01/lineas_pedido.csv). El contrato actual declara: un pedido por fila, `pedido_id` único y no nulo, fecha UTC no nula para pedidos pagados, y canales permitidos `web`, `app`, `partner`.

## Parte A — Grano y métricas

1. Completa el grano de `pedidos` y `lineas_pedido`.
2. ¿Qué clave identifica cada tabla? ¿Qué columna las conecta?
3. Sin contar el duplicado de P-102, ¿cuántos pedidos **pagados con fecha conocida** hay y cuál es su ingreso? Explica por qué decides excluir o no P-103.

## Parte B — Calidad y contrato

4. Identifica todas las reglas del contrato que fallan. Para cada una, anota dimensión de calidad, severidad propuesta, evidencia y acción prudente. No vale responder simplemente «borrar».
5. ¿Qué pregunta deberías hacer a Growth sobre el valor `affiliate`? ¿Por qué normalizarlo automáticamente como `partner` puede ser incorrecto?

## Parte C — Relaciones

6. Si unes `pedidos` con `lineas_pedido` por `pedido_id`, ¿cuál será el grano del resultado? Explica por qué sumar `pedidos.total_eur` después del join puede inflar el ingreso.
7. Propón una forma segura de calcular: a) pedidos pagados e ingreso; b) unidades por producto.

## Parte D — Formatos y responsabilidad

8. El CSV usa `;` y `,`. Indica qué configuración debe conocer quien lo lea y qué error observarías si interpreta mal el separador.
9. A partir de `pedido-ejemplo.json`, enumera las dos tablas que crearías y sus columnas mínimas. ¿Qué dato personal no necesitas para el dashboard pedido por canal?
10. Redacta tres líneas de trazabilidad que acompañarían el reporte final: fuente/versión, reglas aplicadas y límite comunicado.

Consulta solo después [la solución razonada](../../../soluciones/temario-01/auditoria-marketplace.md).
