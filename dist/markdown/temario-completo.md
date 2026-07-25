# Temario completo - Curso de Analista de Datos con Python

# Bloque 00 - Orientación y pensamiento analítico

## Objetivo

Entender qué hace un analista de datos, cómo se formula una pregunta útil y cómo aprovechar este curso sin depender siempre de un ordenador.

## Qué hace un analista

Un analista convierte una necesidad de decisión en evidencia comprensible. No consiste en hacer gráficos bonitos ni en ejecutar consultas aisladas. El trabajo habitual sigue un ciclo:

1. Aclarar la decisión que se quiere tomar.
2. Definir una pregunta medible y las métricas relevantes.
3. Localizar, comprender y preparar los datos.
4. Analizar, comprobar supuestos y comunicar límites.
5. Recomendar una acción y medir qué ocurrió después.

## De una petición vaga a una pregunta analítica

Una frase como "las ventas van mal" no es todavía una pregunta analítica. Hay que concretar periodo, segmento, referencia y decisión. Por ejemplo: "¿Qué canales explican la caída del 12 % de ventas de junio frente al promedio de marzo a mayo, y qué acción puede recuperar margen sin aumentar el gasto total?".

Una buena pregunta incluye población, métrica, periodo y comparación. Si falta uno de esos elementos, pide contexto antes de calcular.

## Métricas desde el primer día

Una métrica es una medida definida de forma reproducible. Un KPI es una métrica elegida para seguir un objetivo importante. Antes de aceptar una cifra pregunta:

- ¿Cuál es la fórmula exacta?
- ¿Qué población incluye y excluye?
- ¿Qué intervalo temporal usa?
- ¿De qué fuente procede y cuándo se actualizó?
- ¿Qué decisión cambiaría si el valor sube o baja?

## Herramientas y modo de estudio

La teoría se lee desde GitHub o en PDF. Los notebooks se pueden abrir con Google Colab desde navegador. Para un trabajo profesional también necesitarás aprender a documentar decisiones, trabajar con tickets y colaborar mediante GitHub o Jira; se abordará más adelante.

## Resumen

El análisis empieza por una decisión, no por una herramienta. Define la pregunta y la métrica antes de abrir Python.

## Ejercicios

Realiza [los ejercicios de comprensión](../../ejercicios/temario-00/comprension/preguntas.md) antes de consultar [las soluciones](../../soluciones/temario-00/preguntas.md).

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

# Bloque 02 - Python desde cero

## Objetivo

Aprender a leer, escribir y depurar pequeños programas de Python orientados a datos.

## Ejecutar Python

Un notebook mezcla texto, código y resultados. Puedes ejecutarlo en Google Colab desde el navegador. Ejecuta una celda, observa el resultado y cambia una sola cosa cada vez cuando estés aprendiendo.

## Valores y variables

Python trabaja con números, texto, booleanos y el valor especial `None`. Una variable da un nombre a un valor:

```python
ventas = 1200
objetivo = 1500
cumplimiento = ventas / objetivo
```

Usa nombres descriptivos. `importe_total` comunica más que `x`.

## Colecciones

Las listas guardan una secuencia ordenada y modificable. Los diccionarios relacionan claves con valores. Para un analista, ambos aparecen con frecuencia al recibir respuestas de APIs o preparar datos antes de pasarlos a Pandas.

```python
canales = ["web", "tienda", "partners"]
venta = {"canal": "web", "importe": 42.50}
```

## Condiciones, bucles y funciones

Una condición selecciona una acción. Un bucle repite una operación. Una función encapsula una tarea reutilizable. Prioriza claridad sobre trucos cortos: tu código debe poder explicarse a otra persona.

```python
def clasificar_venta(importe):
    if importe >= 100:
        return "alta"
    return "normal"
```

## Errores y depuración

Los errores son información. Lee primero la última línea: indica el tipo de error y la causa inmediata. Después comprueba los valores, tipos y nombres de las variables implicadas. No copies una solución de AI sin ejecutar y entender el resultado.

## Resumen

Python permite expresar cálculos de forma reproducible. Primero dominarás piezas pequeñas y después usarás NumPy y Pandas para trabajar con tablas reales.

## Práctica

Abre el [notebook de gastos personales](../../notebooks/practicas/02-gastos-personales.ipynb) o [ejecútalo en Google Colab](https://colab.research.google.com/github/Ayhur/CursoAnalista/blob/main/notebooks/practicas/02-gastos-personales.ipynb). También puedes resolver [el ejercicio](../../ejercicios/temario-02/aplicacion/gastos-personales.md). Las [soluciones](../../soluciones/temario-02/gastos-personales.md) se consultan al terminar.
