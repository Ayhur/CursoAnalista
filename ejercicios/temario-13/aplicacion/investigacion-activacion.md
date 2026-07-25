# Práctica - Investigación reproducible de activación

Nébula lanza la versión 4.2 el 15 de abril. El PM escribe: «Android activaba bien; ahora parece peor. ¿Revertimos?». Dispones de un extracto sintético que el laboratorio genera y de esta pista: el evento `reserva_creada` podría haber cambiado en Android.

## Entrega

Prepara una carpeta o documento con estos seis artefactos. No necesitas Jira, Amplitude ni Power BI instalados: puedes usar tablas Markdown y el script del bloque.

1. Un ticket con decisión, pregunta, métrica, población, fecha de corte, segmentos, fuentes, riesgos, responsable y criterios de aceptación.
2. Un contrato de métrica de activación a siete días: fórmula, grano, exclusiones, zona horaria, versión y propietario.
3. Un extracto de tracking plan para `cuenta_creada` y `reserva_creada`, incluyendo identidad, momento de emisión, propiedades, reglas y dueño.
4. Una propuesta de estructura de proyecto y dos commits con mensajes que representen unidades de cambio.
5. Una revisión del resultado del laboratorio: identifica qué versión/plataforma parece peor y qué comprobación de calidad impide concluir causalidad.
6. Una nota de decisión de máximo 180 palabras: recomendación, evidencia, límite, siguiente acción, dueño y métrica/fecha de seguimiento.

## Criterios de evaluación

- No se confunde evento con cuenta ni se cuentan altas sin siete días completos.
- Se declara que una caída observada no prueba causa.
- La propuesta permite reconstruir fuente, script, parámetros y salida sin exponer datos personales.
- La recomendación es proporcional al fallo posible de instrumentación.

Consulta la [solución razonada](../../../soluciones/temario-13/investigacion-activacion.md) solo después de entregar tu versión.
