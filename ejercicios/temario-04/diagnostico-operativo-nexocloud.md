# Ejercicio - Diagnóstico operativo de NexoCloud

## Situación

La matriz `tiempos` contiene minutos medios de primera respuesta. Sus filas son lunes, martes, miércoles y jueves; sus columnas, `web`, `chat` y `correo`, en ese orden. Un `np.nan` significa que el sistema de medición no entregó el dato, no que el tiempo fuera cero.

```python
import numpy as np

canales = np.array(["web", "chat", "correo"])
tiempos = np.array([
    [38.0, 52.0, 110.0],
    [41.0, np.nan, 130.0],
    [44.0, 47.0, 115.0],
    [39.0, 55.0, 125.0],
])
objetivos = np.array([40.0, 45.0, 120.0])
```

## Entregable

Responde por escrito y ejecuta el código que necesites.

1. Escribe el contrato de la matriz: `shape`, significado de cada eje, unidad y el significado de `NaN`.
2. Calcula `desviacion = tiempos - objetivos`. Explica por qué broadcasting aplica el objetivo correcto a cada columna.
3. Crea una máscara de incumplimiento (`tiempos > objetivos`). ¿Qué pares día-canal incumplen? No trates el `NaN` como incumplimiento ni como cumplimiento.
4. Calcula con `np.nanmean` el tiempo medio por canal y el número de valores observados por canal. Explica por qué debes informar ambas cosas juntas.
5. Demuestra con un ejemplo breve la diferencia entre un corte-vista y `.copy()`. ¿Qué riesgo evita la copia en este caso?
6. Propón una recomendación operativa prudente en dos frases: una basada en la evidencia y otra que indique qué falta comprobar antes de atribuir una causa.

## Pista de autoevaluación

La forma esperada de `desviacion` y de la máscara es `(4, 3)`. Si obtienes una forma diferente, vuelve al contrato antes de buscar una alternativa sintáctica.
