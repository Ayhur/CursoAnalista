# Diagramas que usa un analista en una empresa

Los diagramas no sustituyen el análisis: hacen visible cómo fluye la información, quién decide y dónde puede existir un problema. Mantén etiquetas breves, un único propósito por diagrama y una pregunta clara en el título.

## 1. Flujo de proceso

Úsalo para explicar un recorrido: por ejemplo, cómo se transforma una petición de negocio en una decisión.

```mermaid
flowchart TD
    A[Petición de negocio] --> B[Definir pregunta y métrica]
    B --> C[Extraer y validar datos]
    C --> D[Analizar]
    D --> E[Decisión y seguimiento]
```

## 2. Arquitectura de datos

Úsalo para explicar de dónde viene un dato y dónde termina. Es crucial para no pedir a una base operacional una consulta que debería resolverse en un warehouse.

```mermaid
flowchart LR
    A[Aplicación o eventos] --> B[Base operacional]
    B --> C[Pipeline de datos]
    C --> D[Warehouse]
    D --> E[BI, SQL y Python]
    E --> F[Equipo y decisión]
```

## 3. Árbol de métricas

Úsalo para vincular un objetivo con métricas controlables y guardrails.

```mermaid
flowchart TD
    A[Valor semanal entregado] --> B[Activación]
    A --> C[Retención]
    A --> D[Monetización]
    A --> E[Guardrail: calidad]
```

## 4. Límites y propiedad

Cuando un diagrama cruza equipos, indica propietario, sistema fuente y frecuencia de actualización. Un diagrama bonito sin estas tres cosas suele generar dudas en vez de resolverlas.
