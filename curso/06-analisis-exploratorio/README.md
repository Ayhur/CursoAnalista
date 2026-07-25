# Bloque 06 - Análisis exploratorio de datos

## Propósito

El análisis exploratorio de datos (EDA, por *exploratory data analysis*) es la investigación inicial antes de explicar, predecir o cambiar algo. Sirve para responder: «¿qué ha ocurrido realmente en los datos, dónde ocurre y qué datos faltan para entenderlo?». No sirve, por sí solo, para afirmar la causa.

Al terminar podrás transformar una alerta vaga -por ejemplo, «han bajado las compras»- en un informe reproducible que producto, ingeniería o dirección pueda revisar.

## Caso continuo: la incidencia de checkout de Nébula

Nébula es una aplicación de suscripción. El lunes 12 de mayo el panel muestra que la conversión de visita a compra ha pasado de 5,1 % a 4,4 %. Recibimos un archivo: cada fila resume un día, plataforma y canal. A lo largo del bloque usarás ese mismo archivo para comprobar si la caída es real, localizar segmentos afectados, detectar valores sospechosos y proponer la siguiente comprobación.

> **Antes de empezar.** Una *fila* es un registro; aquí representa «un día para una plataforma y un canal». Una *columna* guarda una característica de esas filas, como `visitas` o `compras`. El archivo CSV es texto con valores separados por comas: se parece a una tabla de hoja de cálculo, pero puede abrirse con un editor o con Python. El bloque 05 explica cómo cargarlo con Pandas.

## Resultados observables

- escribir una pregunta exploratoria, su periodo y su unidad de observación;
- perfilar una fuente: filas, columnas, cobertura, nulos, duplicados, rangos y definiciones;
- describir distribuciones y segmentos sin ocultar el total ni los denominadores;
- distinguir un hallazgo, una asociación y una afirmación causal;
- decidir qué hacer con un valor extremo dejando una regla trazable;
- entregar una nota de hallazgos, límites y próxima acción junto con código reproducible.

## Prerrequisitos

Necesitas los conceptos de tabla, tipos de dato y calidad del bloque 01, Python básico del bloque 02 y carga/manipulación elemental con Pandas del bloque 05. No necesitas estadística inferencial: la aprenderás en el bloque 08.

## Ruta de lecciones

1. [De una alerta a una pregunta y un perfil reproducible](lecciones/01-preguntas-y-perfil-exploratorio.md)
2. [Distribuciones, denominadores y segmentación](lecciones/02-distribuciones-segmentos-y-outliers.md)
3. [Valores extremos: investigar antes de borrar](lecciones/03-valores-extremos-y-calidad.md)
4. [Relaciones, correlación, causalidad y paradoja de Simpson](lecciones/04-relaciones-correlacion-y-causalidad.md)
5. [Del hallazgo a una decisión responsable](lecciones/05-registro-de-hallazgos-y-decisiones.md)
6. [Laboratorio: investigar la caída de checkout](lecciones/06-laboratorio-incidencia-checkout.md)

## Material práctico

- [Datos de Nébula](../../datasets/nebula_checkout_mayo.csv)
- [Laboratorio ejecutable](../../notebooks/practicas/06-eda-incidencia-checkout.py)
- [Ejercicio aplicado](../../ejercicios/temario-06/aplicacion/investigar-caida.md)
- [Solución razonada](../../soluciones/temario-06/investigar-caida.md)

## Qué no concluye este bloque

Un patrón descriptivo puede justificar abrir una incidencia, priorizar una comprobación o diseñar un experimento. No demuestra que una versión, un canal o una campaña haya causado el cambio. Esa frontera es la diferencia entre un análisis útil y una decisión precipitada.
