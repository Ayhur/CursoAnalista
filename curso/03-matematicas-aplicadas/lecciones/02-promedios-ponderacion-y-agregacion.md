# Promedios, ponderación y agregación

## Objetivos y prerrequisitos

Aprenderás cuándo un promedio resume un conjunto y cuándo lo distorsiona. Requiere comprender porcentajes y tasas.

## Un promedio siempre combina observaciones

La media aritmética suma valores y divide por su número. Es útil para importes comparables, pero una media de tasas puede ser engañosa si cada grupo tiene un tamaño distinto. Si el país A convierte 8 de 10 visitas (80 %) y B convierte 1 000 de 10 000 (10 %), la media simple de 45 % no describe la conversión conjunta. La respuesta correcta suma éxitos y oportunidades: `1008 / 10010`, aproximadamente 10,1 %.

Eso es una **media ponderada**: cada tasa pesa según su denominador. No es un detalle de fórmula; evita tomar decisiones de inversión basadas en segmentos pequeños y extremos.

## Agregar cambia el grano

Antes de sumar o promediar, pregunta qué representa una fila. Si cada fila es un pedido, sumar importes da ingresos por pedido. Si cada fila es un usuario mensual, sumar ingresos puede duplicar clientes que compraron varias veces. El nivel al que se describe un dato se llama **grano** y se estudió en el bloque 01.

## Error habitual: promedio de promedios

Un dashboard muestra conversión diaria y calcula la media de siete porcentajes. Puede ser válido si cada día tiene el mismo tráfico; si no, conviene dividir compras totales entre visitas totales. Conserva numerador y denominador: permiten revisar y reponderar.

## Resumen

El promedio no es neutral: depende de qué observaciones se incluyan y cuánto pesa cada una. Continúa con [funciones, vectores y matrices](03-funciones-vectores-y-matrices.md).
