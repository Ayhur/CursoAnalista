# Bloque 08 — Estadística para decisiones y experimentos

## Propósito

La estadística no es una colección de fórmulas para declarar que un cambio «funciona». Es el lenguaje para separar una señal plausible del ruido, cuantificar cuánto no sabemos y decidir qué riesgo es razonable asumir. En este bloque Leo acompaña a **Nexo**, una aplicación de gestión de tareas. El equipo quiere probar un onboarding B: una lista de tres acciones guiadas en lugar de la pantalla habitual. La pregunta final es concreta: **¿debe lanzarse B para todos los nuevos usuarios, seguir aprendiendo o descartarse?**

El caso usa una métrica binaria: activación dentro de 24 horas. Un usuario está activado (`1`) si crea un proyecto y una tarea; de lo contrario vale `0`. Trabajaremos con usuarios —no sesiones— como unidad de análisis. Esta precisión evita contar a una misma persona varias veces.

## Resultados observables

Al terminar podrás:

- describir una conversión y su variabilidad sin esconder usuarios ni colas importantes;
- distinguir población, muestra, sesgo y azar de asignación;
- estimar una diferencia con un intervalo de confianza e interpretar correctamente un p-valor;
- diseñar y auditar un experimento A/B: contrato, aleatorización, exposición, guardrails y regla de parada;
- traducir puntos porcentuales a valor, coste, incertidumbre y recomendación;
- ejecutar un laboratorio reproducible y defender una decisión limitada por la evidencia.

## Prerrequisitos y mapa

Necesitas porcentajes, media y lectura de tablas de los bloques 01–07. No se presupone vocabulario estadístico. Cuando aparezca una palabra nueva se presenta primero con el problema que resuelve.

```mermaid
flowchart LR
 A[Contrato del experimento] --> B[Datos y descriptiva]
 B --> C[Muestra y azar]
 C --> D[Estimación e intervalo]
 D --> E[Prueba y potencia]
 E --> F[Guardrails y decisión]
```

El diagrama responde «¿en qué orden se construye una decisión defendible?». Un p-valor aparece casi al final: no puede reparar un objetivo mal definido, datos incompletos o una asignación defectuosa.

## Lecciones

1. [Describir una métrica y su variabilidad](lecciones/01-describir-variabilidad.md)
2. [Población, muestra, aleatorización y sesgo](lecciones/02-poblacion-muestra-y-sesgo.md)
3. [Probabilidad, simulación y distribución muestral](lecciones/03-probabilidad-e-incertidumbre.md)
4. [Intervalos, hipótesis y errores de decisión](lecciones/04-intervalos-y-pruebas.md)
5. [Diseñar y operar un experimento A/B](lecciones/05-experimentos-ab.md)
6. [Efecto, tamaño de muestra y recomendación](lecciones/06-tamano-de-efecto-y-decision.md)

## Material práctico

- [Laboratorio ejecutable: experimento de onboarding](../../notebooks/practicas/08-experimento-onboarding.py). Se puede ejecutar con Python 3 sin instalar librerías; también sirve en Replit o Google Colab desde móvil.
- [Ejercicio de decisión](../../ejercicios/temario-08/aplicacion/experimento-onboarding.md) y su [solución razonada](../../soluciones/temario-08/experimento-onboarding.md).

> **Aviso matemático.** Si ya dominas proporciones, varianzas y distribución normal, puedes avanzar más deprisa por las derivaciones. No saltes las interpretaciones, el contrato ni los límites: ahí está la aplicación profesional.
