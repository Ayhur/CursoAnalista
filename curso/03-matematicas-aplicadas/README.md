# Bloque 03 - Matemáticas aplicadas al análisis

## Por qué este bloque existe

Un analista no estudia matemáticas para repetir fórmulas: las utiliza para no confundir una mejora pequeña con una grande, sumar cantidades incompatibles o recomendar una decisión sobre una comparación injusta. Este bloque acompaña un caso continuo: **Nexo**, una aplicación de reparto. Su equipo quiere saber si el aumento de pedidos está mejorando realmente el negocio y si hace falta más capacidad de reparto.

Leo necesita primero poder leer una cifra con seguridad. Después usará estas ideas con NumPy, Pandas, EDA, estadística y series temporales. Si ya manejas matemática universitaria, puedes saltar la demostración elemental, pero no los supuestos, unidades, contraejemplos ni decisiones del caso.

## Resultados observables

Al completar el bloque podrás:

- declarar qué mide una cifra, en qué unidad, sobre qué población y periodo;
- calcular e interpretar cambios absolutos, porcentajes, tasas y puntos porcentuales sin cambiar la base de comparación;
- resumir datos con media, mediana, percentiles, IQR y desviación estándar, explicando cuándo cada resumen engaña;
- construir agregaciones y medias ponderadas que respeten el grano del dato;
- usar una función, vector o matriz como modelo sencillo de un problema de IT;
- comparar tiempo, crecimiento, ventanas y granularidades sin mezclar periodos.

## Prerrequisitos y ruta

No presupone programación. Se usa una **tabla** como una lista ordenada de registros: cada fila representa una observación y cada columna una propiedad. Por ejemplo, una fila puede ser el resumen de pedidos de un día. Los cálculos se muestran a mano primero y después se automatizan en el laboratorio.

## Lecciones

1. [Magnitudes, unidades, porcentajes y tasas](lecciones/01-magnitudes-porcentajes-y-tasas.md)
2. [Describir una distribución: centro, dispersión y percentiles](lecciones/02-descriptiva-y-distribuciones.md)
3. [Ponderación, agregación y el grano del dato](lecciones/03-ponderacion-agregacion-y-grano.md)
4. [Funciones y modelos sencillos para decisiones](lecciones/04-funciones-y-modelos.md)
5. [Vectores, matrices y cálculo por lotes](lecciones/05-vectores-matrices-y-numpy.md)
6. [Tiempo, granularidad, crecimiento y ventanas](lecciones/06-tiempo-granularidad-y-ventanas.md)

## Práctica y laboratorio

- [Caso integrador: capacidad y crecimiento de Nexo](../../ejercicios/temario-03/aplicacion/caso-nexo-capacidad.md)
- [Solución razonada](../../soluciones/temario-03/caso-nexo-capacidad.md)
- [Laboratorio reproducible](../../notebooks/practicas/03-matematicas-nexo.py)

## Criterio de salida

No basta con obtener un número. Una respuesta se considera defendible cuando explica unidad, denominador, periodo, granularidad, tratamiento de ausencias y qué conclusión permite - y cuál no permite.
