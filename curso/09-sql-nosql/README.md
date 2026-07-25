# Bloque 09 - SQL, NoSQL y almacenamiento

## Objetivo

Entender cómo viven los datos en una empresa, consultar tablas con SQL y saber cuándo un modelo documental o clave-valor requiere una forma distinta de pensar.

## SQL para preguntas de negocio

SQL permite seleccionar, filtrar, agrupar, unir y ordenar datos. Para cada consulta define el grano: ¿una fila representa un pedido, un usuario, una sesión o un evento? El grano evita duplicar o perder información al usar `JOIN`.

```mermaid
flowchart LR
    A[Fuente operacional] --> B[Extracción]
    B --> C[Warehouse o lakehouse]
    C --> D[SQL y modelos]
    D --> E[Dashboard, Python o informe]
```

## NoSQL sin mitos

MongoDB almacena documentos flexibles y permite filtros y pipelines de agregación. DynamoDB organiza datos alrededor de claves y patrones de acceso con rendimiento predecible. Son excelentes para algunas aplicaciones operacionales; no reemplazan automáticamente un warehouse orientado a análisis histórico y uniones complejas.

## AI para consultas

MongoDB Atlas puede generar filtros y agregaciones a partir de lenguaje natural. Úsalo como borrador, no como autoridad: revisa semántica, filtros, coste, índices, datos sensibles y resultado. Una consulta que "parece" correcta puede contestar otra pregunta.

## Práctica

Resuelve [la consulta de conversión](../../ejercicios/temario-09/aplicacion/consulta-conversion.md) y compara con [la solución](../../soluciones/temario-09/consulta-conversion.md).
