# Broadcasting, simulación y reproducibilidad

## Objetivos y prerrequisitos

Comprenderás cómo NumPy combina dimensiones compatibles y por qué una simulación debe poder repetirse. Requiere forma y arrays.

## Broadcasting sin magia

**Broadcasting** es la regla por la que NumPy aplica un vector compatible a una matriz sin copiarlo manualmente. Si una matriz contiene ventas por día y canal, restar la media de cada canal puede centrar sus columnas. No memorices casos: imprime `shape` y comprueba qué dimensión representa cada valor antes de operar.

## Simular para explorar, no para fabricar evidencia

Puedes generar números aleatorios para practicar o evaluar un método. Una **semilla** fija el punto de partida del generador y permite repetir el mismo ejemplo:

```python
generador = np.random.default_rng(42)
muestra = generador.normal(loc=100, scale=15, size=5)
```

El 42 no hace la simulación más verdadera; hace el resultado reproducible. Una muestra simulada sirve para aprender o estudiar escenarios, no para afirmar qué hicieron clientes reales.

## Cierre y ejercicio

NumPy permite transformar, seleccionar y resumir números de forma concisa. Antes de Pandas, resuelve una práctica: crea ventas, aplica una máscara y explica qué supuesto contiene el umbral. Documenta semilla y forma. El mismo criterio se aplicará a tablas reales.
