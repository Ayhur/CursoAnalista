# Solución razonada - Lumen Market: ingresos y conversión

## 1. Contrato

Resultado a grano `canal`. Población: pedidos con `estado='pagado'` creados desde `2026-07-01T00:00:00Z` inclusive hasta `2026-07-08T00:00:00Z` exclusive. La fuente de líneas aporta importes vendidos; clientes compradores se deduplican por `cliente_id`. Los pedidos pagados sin liquidación se mantienen visibles como incidencia, no se transforman silenciosamente en cero.

## 2. Ingresos sin multiplicación

```sql
WITH importe_por_pedido AS (
  SELECT pedido_id, SUM(cantidad * precio_unitario) AS importe
  FROM lineas_pedido
  GROUP BY pedido_id
)
SELECT p.canal,
       COUNT(DISTINCT p.pedido_id) AS pedidos_pagados,
       COUNT(DISTINCT p.cliente_id) AS compradores_unicos,
       ROUND(SUM(i.importe), 2) AS ingresos
FROM pedidos p
JOIN importe_por_pedido i ON i.pedido_id = p.pedido_id
WHERE p.estado = 'pagado'
  AND p.creado_en >= '2026-07-01T00:00:00Z'
  AND p.creado_en <  '2026-07-08T00:00:00Z'
GROUP BY p.canal;
```

La CTE tiene una fila por pedido, de modo que sumar `i.importe` una vez por pedido es válido. Un join directo a líneas cambia el grano a línea; sumar una columna repetida de pedido después de ese join lo inflaría.

Con la semilla del laboratorio, app tiene 3 pedidos, 3 compradores e ingresos 50,40; web tiene 1 pedido, 1 comprador e ingresos 4,00. Esos valores son verificaciones del ejercicio, no conclusiones generalizables de negocio.

## 3. Conciliación

```sql
SELECT p.pedido_id, p.cliente_id, p.creado_en
FROM pedidos p
WHERE p.estado = 'pagado'
  AND NOT EXISTS (
    SELECT 1 FROM pagos g
    WHERE g.pedido_id = p.pedido_id AND g.estado = 'liquidado'
  );
```

La semilla devuelve `P104`. Puede ser retraso de carga, estado incorrecto, pago pendiente o defecto de integración. No debe llamarse cero sin contrato financiero; se reporta junto a los ingresos y se investiga.

## 4. Funnel

La unidad es cliente-día (en producción podría ser cliente-semana UTC). Para cada unidad se toma la primera ocurrencia de cada paso y se exige `vista <= checkout <= compra`. `COUNT(*)` de eventos mediría acciones: C002 tiene dos `checkout_started` y una sola persona.

Controles: `cliente_id` no nulo o identidad de sesión documentada; eventos ordenados por instante y con desempate por ID; deduplicación de reintentos; ventana y zona horaria declaradas; revisar que las etapas no aumentan. En la semilla, dos clientes ven producto, dos inician checkout ordenado y solo Ana llega a compra ordenada.

## 5. Elección de almacenamiento

En MongoDB, un pedido cerrado puede incrustar sus líneas para leerlo entero y conservar el precio vendido; el cliente se referencia por `clienteId`, porque cambia y se reutiliza. Un índice se decide por filtros reales, por ejemplo `estado + creadoEn`, tras revisar el plan.

Para DynamoDB: historial de cliente `PK=CLIENTE#C001`, `SK=PEDIDO#<fecha>#<id>`; un GSI de cola puede tener `GSI1PK=ESTADO#pagado#<día>` y `GSI1SK=<fecha>#<pedido_id>`. Evita una PK global caliente. «Ingresos trimestrales por país y cohorte» va a una capa OLAP, que permite historia, transformaciones y agregaciones amplias reproducibles.
