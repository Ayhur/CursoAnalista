# Bloque 12 - Modelos predictivos para analistas

## Propósito

Un modelo predictivo no sustituye el criterio de producto: ordena incertidumbre para que un equipo pueda actuar primero donde el beneficio esperado es mayor. En este bloque Leo acompaña a **Lumen**, una aplicación de suscripción, que solo puede contactar cada semana a una parte de las personas con riesgo de abandono (*churn*).

El caso continuo responde a una pregunta concreta: **cada lunes, ¿qué cuentas conviene priorizar para una revisión humana durante los próximos 30 días?** Aprenderás a convertir esa pregunta en objetivo, datos disponibles, evaluación, umbral operativo y documentación responsable.

## Resultados de aprendizaje

Al terminar podrás:

- distinguir predicción, explicación causal y decisión;
- definir objetivo, población, fecha de corte y variables sin mirar el futuro;
- comparar un baseline con una clasificación sencilla;
- leer matriz de confusión, precision, recall, F1, ROC-AUC y PR-AUC;
- elegir un umbral según capacidad y coste, no por costumbre;
- detectar desbalanceo, fuga, mala calibración y deriva;
- documentar límites mediante una model card.

## Prerrequisitos

Los bloques de Python, Pandas, estadística y métricas. No se presupone experiencia previa con aprendizaje automático: cada palabra nueva se introduce dentro del caso.

## Lecciones

1. [Del problema de negocio al contrato predictivo](lecciones/01-caso-de-uso-y-objetivo.md)
2. [Datos disponibles, partición temporal y fuga](lecciones/02-preparacion-y-fuga.md)
3. [Baselines, clasificación y modelos sencillos](lecciones/03-baselines-y-modelos.md)
4. [Métricas, umbrales, capacidad y calibración](lecciones/04-evaluacion-y-coste-de-error.md)
5. [Interpretación, sesgo, deriva y model card](lecciones/05-interpretacion-sesgo-y-uso-responsable.md)

## Material aplicado

- [Datos de ejemplo de Lumen](../../datasets/lumen_churn_ejemplo.csv): una fila por cuenta en una fecha de corte.
- [Laboratorio reproducible](../../notebooks/practicas/12-priorizacion-churn.py): ejecutable con `python` y sin instalar librerías.
- [Ejercicio de priorización](../../ejercicios/temario-12/aplicacion/priorizar-churn.md) y su [solución razonada](../../soluciones/temario-12/priorizar-churn.md).

## Regla profesional del bloque

Una probabilidad no es una orden automática. Antes de contactar, excluir, subir precio o negar una oportunidad, pregunta: «¿qué sabíamos al predecir, qué daño puede causar el error y quién revisa la decisión?».
