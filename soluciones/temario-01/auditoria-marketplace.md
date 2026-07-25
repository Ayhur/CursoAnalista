# Solución razonada — Auditoría de Mercado Faro

## Parte A

1. `pedidos`: una fila representa un pedido iniciado; `lineas_pedido`: una fila representa un artículo dentro de un pedido. El segundo grano es más fino: un pedido puede ocupar varias filas.
2. `pedido_id` identifica pedidos; `linea_id` identifica líneas. `lineas_pedido.pedido_id` es la referencia que conecta ambas tablas.
3. Con fecha conocida y estado pagado quedan P-100 y P-102. Tras deduplicar P-102 son **2 pedidos y 107,00 €** (42 + 65). P-103 está pagado pero no tiene fecha: no sabemos con evidencia que pertenezca al día 24. Se debe investigar y reportar como incidencia, no eliminarlo definitivamente.

## Parte B

| Hallazgo | Dimensión | Severidad | Acción |
| --- | --- | --- | --- |
| P-102 aparece dos veces | unicidad | crítica para ingreso diario | bloquear publicación, comprobar reintento de exportación y conservar una versión deduplicada documentada |
| P-103 no tiene `creado_en_utc` | completitud | crítica para métrica por día | recuperar fecha desde sistema fuente o excluir solo de esa métrica y declarar el límite |
| `affiliate` no está en catálogo | consistencia/validez | advertencia | aislar el valor, consultar definición y actualizar contrato si es canal nuevo legítimo |

La pregunta a Growth es «¿`affiliate` representa el mismo mecanismo de atribución que `partner`, desde qué fecha y para qué pedidos?». Cambiarlo sin evidencia destruye trazabilidad y puede ocultar que se lanzó un canal nuevo.

## Parte C

6. El join tiene grano «una línea de pedido». P-100 aparecerá dos veces; si su `total_eur=42` se repite y se suma, aporta 84 € aunque el pedido cobró 42 €. La duplicación es esperable por la relación 1:N, no un fallo del join.
7. Para pedidos e ingreso, calcula sobre `pedidos` una vez deduplicado y filtrado; cuenta `pedido_id` y suma `total_eur`. Para unidades por producto, usa `lineas_pedido` y suma `cantidad` agrupando por `producto_id`. Si se necesita añadir atributos del pedido a las líneas, el join se hace después sabiendo que permanece el grano de línea.

## Parte D

8. Hay que declarar `delimiter=';'`, decimal `','`, codificación UTF-8 y fechas ISO 8601 en UTC. Si el separador se interpreta como coma, la cabecera puede quedar en una única columna; si el decimal no se transforma, `42,00` puede ser texto y no permitir sumas fiables.
9. Del JSON se crean `pedidos(pedido_id, usuario_id, creado_en_utc, estado, total_eur)` y `lineas_pedido(pedido_id, producto_id, cantidad, precio_eur)`. Para el dashboard por canal no se necesita correo, teléfono, dirección ni nombre; idealmente ni siquiera el identificador de usuario.
10. Ejemplo de trazabilidad: «Fuente: exportación Checkout v3 recibida 2026-07-25 08:30 UTC. Se deduplicó P-102 por `pedido_id`; se excluyó P-103 solo del corte diario por fecha ausente. Resultado limitado a pedidos con fecha UTC conocida; `affiliate` permanece sin clasificar hasta confirmación de Growth».

La respuesta correcta no es solo llegar a 107 €. Es poder explicar por qué esa cifra cambia si aparece evidencia nueva y qué se decidió no afirmar.
