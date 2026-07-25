# Seleccionar, filtrar y resumir con SQL

## Objetivos y prerrequisitos

Escribirás una consulta legible que responda una pregunta concreta y comprobarás qué filas excluye.

SQL es un lenguaje declarativo: describes qué resultado quieres, no los pasos internos exactos. Para contar pedidos pagados por canal:

```sql
SELECT canal, COUNT(*) AS pedidos
FROM pedidos
WHERE estado = 'pagado'
GROUP BY canal
ORDER BY pedidos DESC;
```

`WHERE` filtra filas antes de agrupar; `GROUP BY` define el nivel del resultado. `COUNT(*)` cuenta filas, pero `COUNT(DISTINCT pedido_id)` cuenta pedidos únicos. Elegir uno es una definición de métrica, no una preferencia sintáctica.

## Error habitual

Filtrar un periodo con texto o sin zona horaria explícita puede incluir o excluir registros inesperados. Inspecciona datos de borde y declara la ventana temporal.

## Resumen

Una consulta profesional hace visibles medida, población y grano. Continúa con [JOIN y cardinalidad](03-joins-y-cardinalidad.md).
