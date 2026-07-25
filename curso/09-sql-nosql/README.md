# Bloque 09 - SQL, NoSQL y almacenamiento

## Propósito

Una empresa no almacena los datos para que un analista pueda hacer una consulta bonita: los almacena primero para cobrar, servir una pantalla o registrar una acción. Este bloque enseña a distinguir esos objetivos y a consultar sin alterar el significado del dato.

Seguiremos a **Lumen Market**, una app de comercio. Sus clientes hacen pedidos, cada pedido tiene líneas, puede tener un pago y deja eventos de producto. Con ese caso aprenderás SQL sobre una base local reproducible y decidirás cuándo un documento MongoDB o una tabla DynamoDB es apropiada. No se presupone que sepas qué es una tabla, un archivo o una clave: cada uno se introduce en contexto.

## Resultados observables

Al terminar podrás:

- declarar el grano, la clave primaria y la cardinalidad antes de escribir SQL;
- ejecutar y explicar una consulta con filtros, agrupaciones, `CASE`, `HAVING`, `JOIN`, CTE y ventanas;
- detectar duplicación, ausencias y definiciones de funnel incompatibles;
- modelar un pedido como documento y justificar *embedding* frente a referencias;
- partir de patrones de acceso para proponer claves y un GSI de DynamoDB, sin confundirlo con un warehouse;
- explicar por qué los datos OLTP de una aplicación suelen transformarse antes de un análisis OLAP.

## Caso y laboratorio

El laboratorio [Lumen Market SQL](../../notebooks/practicas/09-lumen-market-sql.py) crea una base SQLite temporal con DDL y datos semilla. No instala nada: ejecuta `python notebooks/practicas/09-lumen-market-sql.py`. SQLite usa SQL estándar en gran parte; en la lección se indican las diferencias cuando DuckDB o un warehouse ofrecen otra sintaxis.

## Lecciones

1. [Modelo relacional, grano y ERD](lecciones/01-modelo-relacional-y-grano.md)
2. [SQL básico: seleccionar, filtrar y resumir](lecciones/02-sql-seleccion-filtro-y-agregacion.md)
3. [JOIN, cardinalidad y anti-joins](lecciones/03-joins-y-cardinalidad.md)
4. [CTE, ventanas, fechas, nulos y funnel](lecciones/04-sql-analitico-y-mantenible.md)
5. [MongoDB: documentos, pipeline e índices](lecciones/05-mongodb-y-documentos.md)
6. [DynamoDB: patrones de acceso, claves y GSI](lecciones/06-dynamodb-y-patrones-de-acceso.md)
7. [OLTP, OLAP, warehouse, lakehouse y AI](lecciones/07-arquitectura-y-consultas-asistidas.md)

## Práctica evaluable

Resuelve el [caso de ingresos y conversión](../../ejercicios/temario-09/aplicacion/consulta-conversion.md) sin mirar la [solución razonada](../../soluciones/temario-09/consulta-conversion.md). La competencia se evalúa por el grano, los controles y la interpretación; no por memorizar palabras clave.
