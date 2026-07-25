# Selección, máscaras y forma

## Objetivos y prerrequisitos

Aprenderás a elegir elementos por posición o condición y a interpretar la forma de un array. Requiere arrays básicos.

## Preguntar una condición a cada elemento

Una **máscara booleana** contiene `True` o `False` para cada posición. Es la traducción de una pregunta: “¿esta venta supera 100?”

```python
ventas = np.array([80, 125, 210])
es_alta = ventas > 100
ventas[es_alta]  # array([125, 210])
```

La máscara es valiosa porque hace visible el criterio. Antes de filtrar pedidos “altos”, define por qué 100 es el límite y revisa cuántos elementos quedan fuera.

La **forma** (`shape`) describe dimensiones. Un array de tres ventas tiene forma `(3,)`; una matriz de dos días y tres métricas puede tener `(2, 3)`. La forma no da significado a filas y columnas: debes documentarlo.

## Error habitual

Una máscara de longitud distinta al array no se puede aplicar correctamente. Más grave aún: una máscara correcta técnicamente puede estar desalineada conceptualmente si proviene de otro periodo o de clientes ordenados de forma distinta.

## Resumen

Seleccionar es formular un criterio. Comprueba siempre forma, orden y significado antes de combinar arrays.
