# Soluciones - Auditoría de calidad

1. Hay formatos de fecha distintos, un importe negativo que requiere contexto, un pedido duplicado, una fecha ausente y valores de canal con mayúsculas inconsistentes.
2. Antes de borrar el negativo hay que saber si representa devolución. Antes de borrar el duplicado hay que comprobar si dos líneas pueden pertenecer al mismo pedido. Para la fecha ausente, revisa la fuente o un campo alternativo de creación.
3. Convertir a minúsculas, eliminar espacios y validar contra un catálogo, por ejemplo `web`, `tienda`, `partner`.
