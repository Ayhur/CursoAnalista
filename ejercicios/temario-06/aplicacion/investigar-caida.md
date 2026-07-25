# Ejercicio aplicado - Investigar la caída de checkout de Nébula

## Situación

Producto ha recibido una alerta: la conversión de checkout de la semana 05-05 a 11-05 parece menor que en la semana anterior. Dispones de `datasets/nebula_checkout_mayo.csv`. Cada fila agrega un día, plataforma y canal; no contiene usuarios individuales ni registros de errores de pago.

## Entrega

Produce una nota de análisis de una página como máximo. Puedes ejecutar `notebooks/practicas/06-eda-incidencia-checkout.py`, pero explica con tus palabras las decisiones.

1. Escribe la pregunta exploratoria con métrica, periodo, comparación y grano.
2. Describe tres controles de perfil que realizarías antes de calcular una tasa.
3. Calcula, o reproduce del script, la conversión de referencia y actual para el total y cada plataforma. Incluye compras y visitas, no solo porcentajes.
4. Señala la observación extrema del archivo. Da dos explicaciones rivales y explica por qué no la borrarías todavía.
5. Formula una hipótesis de producto, una de calidad/tracking y el dato que pedirías para diferenciarlas.
6. Redacta una actualización de tres o cuatro frases para producto e ingeniería: hallazgo, límite y siguiente acción. No atribuyas causalidad.

## Criterio de calidad

Una respuesta correcta no necesita adivinar la causa. Debe preservar los denominadores, distinguir observación de explicación, ser reproducible y proponer una comprobación concreta.
