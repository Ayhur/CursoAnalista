# Funciones, vectores y matrices

## Objetivos y prerrequisitos

Comprenderás las ideas matemáticas que harán legibles NumPy y Pandas: una función transforma entradas; un vector reúne valores; una matriz organiza muchos vectores.

## Transformar entradas en salidas

Una **función** expresa una relación: dado número de clientes y precio, devuelve ingresos. `ingresos(clientes, precio) = clientes × precio`. No afirma que ambas variables sean independientes ni que subir precio no cambie clientes: solo define el cálculo bajo unos supuestos.

Un **vector** es una lista ordenada de valores de la misma clase, por ejemplo las ventas de tres días: `[120, 140, 110]`. Una **matriz** organiza muchas filas de valores: cada fila podría ser un día y cada columna pedidos, ingresos y devoluciones. En código, un array de NumPy permitirá aplicar un cálculo a todos los elementos sin escribir un bucle manual.

## Relación con el análisis

Los objetos matemáticos no sustituyen el significado. Dos columnas con mil números pueden formar una matriz, pero no por ello es razonable sumarlas si una contiene euros y otra minutos. La estructura permite calcular; el contexto decide si el cálculo responde una pregunta válida.

## Resumen y puente

Funciones hacen explícitas transformaciones; vectores y matrices permiten representar muchas observaciones. En el bloque 04 aprenderás a manejarlos eficientemente con NumPy.
