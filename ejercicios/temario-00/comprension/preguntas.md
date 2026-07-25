# Caso integrador - Bloque 00: activación de Lumen

## Situación

Lumen es una app de reservas de espacios de trabajo. El 8 de julio, producto informa de que «la activación ha bajado». El equipo cambió el onboarding Android a la versión 4.2 el 1 de julio. También lanzó una campaña nueva el 3 de julio. El informe preliminar muestra 290 personas con primera reserva entre 1.000 instalaciones de la versión 4.2; en una semana comparable de la versión 4.1 hubo 380 de 1.000. Nadie ha comprobado aún si los eventos se registran bien.

Producto debe decidir el viernes si revierte temporalmente el onboarding Android, si investiga primero el tracking o si espera más evidencia. Ingeniería advierte que revertir tiene coste y que una reversión no debería ocultar un problema de campaña.

## Entrega

Sin mirar la solución, redacta un brief de una o dos páginas usando la [plantilla](../../../curso/00-orientacion/plantillas/brief-analitico.md). Debe contener lo siguiente.

1. Escribe una pregunta analítica que incluya población, resultado, ventana, comparación y decisión. Indica qué tipo de análisis harás primero y por qué.
2. Separa en una tabla tres elementos: hechos observados, al menos tres hipótesis alternativas y la evidencia que pedirías para cada hipótesis. Incluye explícitamente la posibilidad de un fallo de medición.
3. Define el contrato de `activación_7d`: evento del numerador, denominador, exclusiones, grano, ventana/fecha de corte, fuente, propietario, segmentos y dos métricas de protección.
4. Explica dos motivos por los que el 29% frente al 38% no demuestra aún que la versión 4.2 causó la caída.
5. Recomienda una acción para el viernes. Declara tu nivel de certeza, una condición de reversión y un plan de seguimiento de una semana. No se puntúa elegir «revertir» o «no revertir», sino justificar una decisión proporcional a la evidencia.

## Autoevaluación antes de mirar la solución

- ¿Podría una persona distinta reproducir tu métrica sin preguntarte qué cuenta?
- ¿Has distinguido una observación de una explicación?
- ¿Tu recomendación dice qué se medirá después y qué resultado la haría cambiar?

Consulta después la [solución razonada y rúbrica](../../../soluciones/temario-00/preguntas.md).
