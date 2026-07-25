# JOIN y validación de cardinalidad

## Objetivos y prerrequisitos

Combinarás tablas sin multiplicar accidentalmente registros.

Un `JOIN` une filas por una clave. `INNER JOIN` conserva coincidencias; `LEFT JOIN` conserva todas las filas izquierdas y muestra ausencia de coincidencia. Antes de unir, declara cardinalidad: uno a uno, uno a muchos o muchos a muchos.

```sql
SELECT p.pedido_id, c.pais
FROM pedidos p
LEFT JOIN clientes c ON p.cliente_id = c.cliente_id;
```

Si `clientes` contiene dos filas para el mismo `cliente_id`, cada pedido aparecerá dos veces. Comprueba recuento antes y después, claves duplicadas y nulos introducidos por la unión. Un SQL que ejecuta no prueba que el resultado sea válido.

## Resumen

La cardinalidad es un supuesto analítico que debes validar. Sigue con [SQL analítico](04-sql-analitico-y-mantenible.md).
