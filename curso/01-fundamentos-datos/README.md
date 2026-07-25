# Bloque 01 - Fundamentos de datos

## Objetivo

Reconocer qué representa un conjunto de datos, evaluar su calidad y evitar conclusiones que los datos no permiten.

## Anatomía de una tabla

Una observación suele ser una fila: por ejemplo, una compra. Una variable es una columna: fecha, importe o canal. Una clave identifica de forma única una observación; una clave mal definida crea duplicados y totales erróneos.

Las variables pueden ser numéricas, categóricas, texto, fecha/hora o booleanas. El tipo no es un detalle técnico: determina qué cálculos y visualizaciones tienen sentido.

## Calidad del dato

Antes de analizar, revisa cinco dimensiones:

- Completitud: ¿faltan valores necesarios?
- Validez: ¿los valores respetan reglas, unidades y formatos?
- Consistencia: ¿la misma idea está codificada igual en todo el conjunto?
- Unicidad: ¿hay duplicados indebidos?
- Actualidad: ¿el dato es suficientemente reciente para la decisión?

No elimines valores ausentes por costumbre. Primero averigua por qué faltan y si el patrón de ausencia puede sesgar el resultado.

## Archivos y bases de datos

CSV es simple y común, pero no conserva todos los tipos. JSON representa estructuras anidadas. Excel es útil para tareas ligeras y revisión manual. Parquet almacena datos de forma columnar y suele ser eficiente en análisis.

Las bases relacionales organizan tablas conectadas por claves y se consultan con SQL. Las bases documentales como MongoDB almacenan documentos flexibles. DynamoDB es una base NoSQL de clave-valor y documentos orientada a patrones de acceso. Ninguna tecnología elimina la necesidad de comprender la semántica de los datos.

## Ética y privacidad

Que se pueda acceder a un dato no significa que se deba usar. Minimiza la información personal, evita compartir identificadores en notebooks y piensa a quién puede perjudicar una clasificación o recomendación.

## Resumen

El análisis fiable empieza por saber qué mide cada columna y por comprobar la calidad de los datos antes de calcular promedios.

## Ejercicios

Realiza [la auditoría de calidad](../../ejercicios/temario-01/comprension/auditoria-calidad.md) antes de consultar [las soluciones](../../soluciones/temario-01/auditoria-calidad.md).
