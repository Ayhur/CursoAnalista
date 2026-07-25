# Uniones y cardinalidad

## Objetivos y prerrequisitos

Combinarás tablas comprobando qué clave conecta las filas y cuántas coincidencias son válidas.

Una unión (`merge`) cruza dos tablas mediante una **clave**, por ejemplo `cliente_id`. Antes de ejecutarla declara la cardinalidad: uno a uno, uno a muchos o muchos a uno. Muchos a muchos puede ser correcto, pero multiplica combinaciones y requiere una justificación explícita.

```python
pedidos_con_clientes = pedidos.merge(
    clientes, on="cliente_id", how="left", validate="many_to_one"
)
```

`validate="many_to_one"` convierte un supuesto en una comprobación: muchos pedidos pueden corresponder a un cliente, pero cada pedido no debe encontrar dos fichas de cliente. Tras unir, compara filas, claves sin coincidencia y totales monetarios.

## Error habitual

Ver una columna nueva y asumir que la unión funcionó. Si `clientes` tiene duplicados por error, cada pedido puede repetirse y los ingresos se inflan. La sintaxis válida no demuestra una relación válida.

Continúa con [validación y trazabilidad](05-validacion-y-trazabilidad.md).
