# Bloque 14 - Nivel avanzado: decidir con evidencia imperfecta

## Propósito

Este bloque reúne problemas que no se resuelven con una gráfica ni con una consulta: una caída de conversión que podría ser producto, marketing o un error de medición; un intervalo incierto; una alerta que debe acabar en una acción; y datos que ya no caben cómodamente en un archivo local.

El caso continuo es **Lumen**, una app de reservas. El 8 de junio la conversión de visita a reserva baja de 4,8 % a 3,6 %. El equipo quiere saber si el nuevo formulario la causó, cuánto confiar en la estimación, cuándo alertar y cómo analizar eventos masivos y datos externos sin crear nuevas fugas o riesgos de privacidad.

## Resultados observables

Al terminar podrás formular un estimando causal y su contrafactual, dibujar un DAG y nombrar sus supuestos; construir un intervalo bootstrap y un análisis de sensibilidad; convertir una anomalía en una alerta con runbook; y consultar datos particionados con criterio. También podrás extraer una API paginada de forma reproducible y tratar coordenadas sin confundir sistemas de referencia ni exponer información personal.

## Prerrequisitos

Conviene haber cursado estadística, SQL, métricas y series temporales. No se presupone experiencia con Parquet, DuckDB, APIs ni sistemas de referencia de coordenadas: se presentan desde el problema que resuelven.

## Lecciones

1. [Causalidad: contrafactuales, DAG y diseños](lecciones/01-preguntas-causales-y-disenos.md)
2. [Bootstrap, incertidumbre y sensibilidad](lecciones/02-bootstrap-y-sensibilidad.md)
3. [Anomalías, alertas y runbooks](lecciones/03-anomalias-monitorizacion-y-alertas.md)
4. [Escala: Parquet, particiones y DuckDB](lecciones/04-escala-formatos-y-motores.md)
5. [APIs, datos geoespaciales y fuentes externas](lecciones/05-apis-geoespacial-y-datos-externos.md)

## Práctica integrada

Realiza el [laboratorio de investigación de la caída](../../ejercicios/temario-14/aplicacion/investigar-caida-conversion.md) antes de consultar la [solución razonada](../../soluciones/temario-14/investigar-caida-conversion.md). El script [14-caida-conversion.py](../../notebooks/practicas/14-caida-conversion.py) ilustra los cálculos de bootstrap y el diseño de una alerta, pero no sustituye el razonamiento causal.
