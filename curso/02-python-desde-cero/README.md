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
