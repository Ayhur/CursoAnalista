"""Laboratorio reproducible del bloque 09.

Ejecuta: python notebooks/practicas/09-lumen-market-sql.py
Usa solo la biblioteca estándar; SQLite crea una base temporal en memoria.
"""
import sqlite3


def show(connection, title, query):
    print(f"\n--- {title} ---")
    rows = connection.execute(query).fetchall()
    if not rows:
        print("(sin filas)")
        return
    print(" | ".join(rows[0].keys()))
    for row in rows:
        print(" | ".join(str(value) if value is not None else "NULL" for value in row))


db = sqlite3.connect(":memory:")
db.row_factory = sqlite3.Row
db.executescript("""
PRAGMA foreign_keys = ON;
CREATE TABLE clientes (
  cliente_id TEXT PRIMARY KEY, nombre TEXT NOT NULL, pais TEXT NOT NULL
);
CREATE TABLE pedidos (
  pedido_id TEXT PRIMARY KEY, cliente_id TEXT NOT NULL REFERENCES clientes(cliente_id),
  creado_en TEXT NOT NULL, canal TEXT NOT NULL,
  estado TEXT NOT NULL CHECK(estado IN ('pagado','cancelado'))
);
CREATE TABLE lineas_pedido (
  linea_id INTEGER PRIMARY KEY, pedido_id TEXT NOT NULL REFERENCES pedidos(pedido_id),
  producto TEXT NOT NULL, cantidad INTEGER NOT NULL CHECK(cantidad > 0),
  precio_unitario REAL NOT NULL CHECK(precio_unitario >= 0)
);
CREATE TABLE pagos (
  pago_id TEXT PRIMARY KEY, pedido_id TEXT NOT NULL UNIQUE REFERENCES pedidos(pedido_id),
  importe REAL NOT NULL, estado TEXT NOT NULL
);
CREATE TABLE eventos (
  evento_id TEXT PRIMARY KEY, cliente_id TEXT, evento TEXT NOT NULL, ocurrido_en TEXT NOT NULL
);
INSERT INTO clientes VALUES ('C001','Ana','ES'),('C002','Bruno','ES'),('C003','Carla','PT');
INSERT INTO pedidos VALUES
 ('P100','C001','2026-07-01T10:15:00Z','app','pagado'),
 ('P101','C001','2026-07-03T12:00:00Z','web','pagado'),
 ('P102','C002','2026-07-03T15:30:00Z','app','pagado'),
 ('P103','C003','2026-07-04T09:00:00Z','web','cancelado'),
 ('P104','C003','2026-07-05T17:00:00Z','app','pagado');
INSERT INTO lineas_pedido VALUES
 (1,'P100','cafe',2,4.00),(2,'P100','te',1,4.40),(3,'P101','cafe',1,4.00),
 (4,'P102','libro',1,22.00),(5,'P102','cafe',1,4.00),(6,'P103','te',1,4.40),
 (7,'P104','cafe',3,4.00);
INSERT INTO pagos VALUES
 ('G100','P100',12.40,'liquidado'),('G101','P101',4.00,'liquidado'),
 ('G102','P102',26.00,'liquidado');
INSERT INTO eventos VALUES
 ('E01','C001','view_product','2026-07-01T09:00:00Z'),
 ('E02','C001','checkout_started','2026-07-01T10:00:00Z'),
 ('E03','C001','purchase','2026-07-01T10:15:00Z'),
 ('E04','C002','view_product','2026-07-03T14:00:00Z'),
 ('E05','C002','checkout_started','2026-07-03T15:00:00Z'),
 ('E06','C002','checkout_started','2026-07-03T15:05:00Z'),
 ('E07','C003','purchase','2026-07-04T09:00:00Z');
""")

show(db, "Pedidos pagados por canal (GROUP BY + HAVING)", """
SELECT canal, COUNT(*) AS pedidos
FROM pedidos WHERE estado='pagado'
GROUP BY canal HAVING COUNT(*) >= 1 ORDER BY pedidos DESC, canal;
""")
show(db, "Importe por pedido (grano: pedido)", """
SELECT p.pedido_id, p.cliente_id, ROUND(SUM(l.cantidad*l.precio_unitario), 2) AS importe
FROM pedidos p JOIN lineas_pedido l USING(pedido_id)
WHERE p.estado='pagado' GROUP BY p.pedido_id, p.cliente_id ORDER BY p.pedido_id;
""")
show(db, "Anti-join: pedidos pagados sin pago liquidado", """
SELECT p.pedido_id FROM pedidos p
WHERE p.estado='pagado' AND NOT EXISTS (
 SELECT 1 FROM pagos g WHERE g.pedido_id=p.pedido_id AND g.estado='liquidado'
);
""")
show(db, "Ventanas: pedido y gasto anterior por cliente", """
WITH importe AS (
 SELECT pedido_id, SUM(cantidad*precio_unitario) AS total FROM lineas_pedido GROUP BY pedido_id
)
SELECT p.cliente_id, p.pedido_id, i.total,
 ROW_NUMBER() OVER(PARTITION BY p.cliente_id ORDER BY p.creado_en, p.pedido_id) AS n_pedido,
 LAG(i.total) OVER(PARTITION BY p.cliente_id ORDER BY p.creado_en, p.pedido_id) AS total_anterior
FROM pedidos p JOIN importe i USING(pedido_id) WHERE p.estado='pagado';
""")
show(db, "Funnel validado por cliente y día", """
WITH pasos AS (
 SELECT cliente_id, substr(ocurrido_en,1,10) AS dia,
  MIN(CASE WHEN evento='view_product' THEN ocurrido_en END) AS vista,
  MIN(CASE WHEN evento='checkout_started' THEN ocurrido_en END) AS checkout,
  MIN(CASE WHEN evento='purchase' THEN ocurrido_en END) AS compra
 FROM eventos GROUP BY cliente_id, substr(ocurrido_en,1,10)
)
SELECT COUNT(*) AS clientes_con_vista,
 SUM(CASE WHEN checkout >= vista THEN 1 ELSE 0 END) AS checkout_ordenado,
 SUM(CASE WHEN compra >= checkout AND checkout >= vista THEN 1 ELSE 0 END) AS compra_ordenada
FROM pasos WHERE vista IS NOT NULL;
""")
print("\nLaboratorio terminado. P104 debe aparecer como anomalía de pago: es un control, no un cero automático.")
