# Bloque 05 - Pandas: datos tabulares fiables

## Propósito

Una empresa no necesita que alguien «limpie un Excel»: necesita poder responder, sin cambiar la respuesta cada vez, cuántos pedidos válidos hubo, qué ingresos representan y qué información falta. En este bloque Leo trabaja como analista de **Nébula**, una aplicación de suscripción que vende complementos. Recibirá exportaciones de pedidos y clientes, construirá una tabla analítica y dejará evidencia de cada decisión.

Pandas es una biblioteca de Python para trabajar con tablas. No decide qué dato es correcto: convierte reglas de negocio explícitas en transformaciones repetibles y comprobaciones que pueden fallar.

## Resultado de salida y prerrequisitos

Al terminar podrás cargar un CSV realista, diagnosticarlo, limpiarlo sin perder el original, combinarlo con clientes y publicar una tabla de ingresos por canal reconciliada con el detalle. Necesitas los conceptos de fila, columna, clave, nulo y Python básico de los bloques 01 y 02.

El caso usa los archivos [pedidos_nebula.csv](../../datasets/pandas/pedidos_nebula.csv) y [clientes_nebula.csv](../../datasets/pandas/clientes_nebula.csv). Son pequeños deliberadamente: permiten inspeccionar cada anomalía antes de automatizarla.

## Itinerario

1. [Importar y perfilar una tabla](lecciones/01-dataframes-importacion-y-perfilado.md)
2. [Seleccionar, tipar y limpiar sin ocultar pérdidas](lecciones/02-seleccion-tipos-y-limpieza.md)
3. [Transformar, agrupar y reconciliar una métrica](lecciones/03-transformacion-y-agregacion.md)
4. [Unir tablas y proteger la cardinalidad](lecciones/04-uniones-y-cardinalidad.md)
5. [Contrato de datos, validación y linaje](lecciones/05-validacion-y-trazabilidad.md)
6. [Laboratorio: pipeline de pedidos de Nébula](lecciones/06-caso-integrado-pedidos.md)

## Práctica

Primero ejecuta el [laboratorio reproducible](../../notebooks/practicas/05-pipeline-pedidos-nebula.py). Después resuelve [la auditoría de pedidos](../../ejercicios/temario-05/aplicacion/auditoria-pedidos-nebula.md) sin mirar la [solución razonada](../../soluciones/temario-05/auditoria-pedidos-nebula.md).

## Documentación primaria

- [Pandas: lectura de CSV](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [Pandas: merge, join y compare](https://pandas.pydata.org/docs/user_guide/merging.html)
- [Pandas: Copy-on-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html)
