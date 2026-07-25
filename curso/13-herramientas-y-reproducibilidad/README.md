# Bloque 13 - Herramientas y reproducibilidad

## Objetivo

Trabajar como analista dentro de un equipo: convertir peticiones en entregables verificables, documentar decisiones y hacer que un análisis pueda repetirse.

## De ticket a entrega

Jira, Linear u otras herramientas no son solo listas de tareas. Una petición analítica debe expresar contexto, decisión, métrica, alcance, criterio de aceptación y responsable. Si falta la decisión, el análisis corre el riesgo de ser interesante pero inútil.

```mermaid
flowchart LR
    A[Ticket o petición] --> B[Pregunta y criterios]
    B --> C[Datos y análisis]
    C --> D[Revisión]
    D --> E[Dashboard, informe o decisión]
    E --> F[Seguimiento]
```

## Git y proyectos analíticos

Git registra cambios en código, documentación y definiciones. Un análisis reproducible separa datos no versionados, código, dependencias, resultados derivados y documentación. Los notebooks sirven para explorar y explicar; la lógica repetida conviene moverla a funciones o scripts comprobables.

## Instrumentación y producto

Herramientas como Amplitude permiten revisar eventos, propiedades, funnels, cohorts y retención. Antes de crear un gráfico, valida el tracking plan: nombre del evento, momento de envío, identidad, propiedades y cobertura. Un dashboard no arregla eventos mal definidos.

## BI y comunicación

Power BI, Tableau, Looker y hojas de cálculo cambian de interfaz, pero comparten lo esencial: modelo de datos, métricas definidas, filtros claros, actualización conocida y audiencia. Entrega siempre contexto, recomendación, límites y enlace al detalle.

## Práctica

Redacta [un ticket analítico completo](../../ejercicios/temario-13/aplicacion/ticket-analitico.md).
