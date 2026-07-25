# Datos, variables y fuga de información

## Objetivos y prerrequisitos

Definirás objetivo, momento de predicción y variables que estarían disponibles entonces.

La **variable objetivo** es lo que se quiere estimar; las variables de entrada describen información disponible antes del resultado. Una **fuga de información** ocurre cuando el modelo usa un dato que solo existe después: una cancelación registrada tras el momento en que querías predecir churn.

Separa entrenamiento, validación y prueba respetando tiempo cuando corresponda. Ajustar transformaciones solo con entrenamiento evita que información del futuro mejore artificialmente la evaluación.

## Error habitual

Crear una variable con “número de tickets resueltos” para predecir una baja cuando esos tickets se abren precisamente al iniciar la baja. Un resultado excelente puede ser señal de fuga, no de inteligencia.

## Resumen

La pregunta correcta es: “¿qué sabíamos en el instante de decidir?”.
