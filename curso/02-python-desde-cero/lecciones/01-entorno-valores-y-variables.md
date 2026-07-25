# Ejecutar código, valores y variables

## Objetivos y prerrequisitos

Aprenderás qué hace un programa, cómo ejecutar una celda de notebook y cómo guardar un resultado con un nombre. No necesitas experiencia previa.

## Código que transforma valores

Un programa es una lista de instrucciones que transforma información. En un análisis, esa información puede ser el importe de una compra, una fecha o una respuesta de usuario. Un **valor** es una pieza concreta de información: `1200`, `"web"` o `True` (verdadero).

En Google Colab, un notebook muestra una celda de código y su resultado. Ejecuta primero esto y cambia después un único valor:

```python
ventas = 1200
objetivo = 1500
cumplimiento = ventas / objetivo
print(cumplimiento)
```

Una **variable** es un nombre que referencia un valor. Aquí `cumplimiento` guarda el resultado `0.8`. El signo `=` no pregunta si dos cosas son iguales: asigna el valor de la derecha al nombre de la izquierda.

## Tipos: la forma del dato importa

Python distingue números enteros (`3`), decimales (`3.5`), texto (`"Madrid"`), booleanos (`True` o `False`) y ausencia representada por `None`. El tipo condiciona qué operaciones tienen sentido: sumar `3 + 5` es válido; sumar `"3" + "5"` une texto y produce `"35"`.

Esta secuencia responde a “¿por qué revisar el tipo antes de calcular?”

```mermaid
flowchart LR
  A[Valor recibido] --> B[Comprobar tipo]
  B --> C[Aplicar operación]
  C --> D[Revisar resultado]
```

El paso de comprobar evita, por ejemplo, tratar un importe escrito como texto como si fuera dinero calculable.

## Error habitual

`ventas = ventas + 100` parece una igualdad matemática imposible. En programación significa “toma el valor actual de ventas, súmale 100 y guarda el nuevo resultado bajo el mismo nombre”. Usarlo sin cuidado puede ocultar el valor original; cuando importe, conserva ambos nombres: `ventas_iniciales` y `ventas_actualizadas`.

## Resumen y comprobación

- Una celda ejecuta instrucciones y muestra un resultado.
- Una variable etiqueta un valor; no es una caja mágica independiente.
- El tipo determina qué cálculo es válido.

Prueba `type(ventas)` y `type("1200")`. Explica por qué se diferencian. Continúa con [colecciones](02-colecciones-y-datos-sencillos.md).
