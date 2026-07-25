# Programa docente - Analista de Datos aplicado a IT

## Propósito y nivel de exigencia

Este no es un índice de lectura rápida. Es un itinerario profesional progresivo para formar a un analista capaz de trabajar en equipos tecnológicos: formular problemas, modelar datos, usar Python y SQL, definir métricas, cuestionar evidencia y comunicar una recomendación verificable.

El programa contiene **16 bloques y 161 temas nucleares**. Los temas se agrupan en lecciones para que el alumno pueda aprender una idea completa antes de saltar a la siguiente. Cada bloque tiene un proyecto o prueba de dominio; cada lección no se considera terminada hasta que incluye ejemplos, contraejemplos, práctica y al menos un recurso visual cuando el concepto tenga estructura, flujo o relación entre entidades.

## Estándar de una lección

Una lección no puede limitarse a una definición. Debe incluir:

1. Objetivos, prerrequisitos y resultado observable.
2. Explicación conceptual rigurosa y vocabulario.
3. Ejemplo aplicado a una empresa tecnológica.
4. Un diagrama integrado en la explicación cuando aporte comprensión: flujo, arquitectura, modelo de datos, árbol de decisión o relación causal.
5. Errores y falsas intuiciones frecuentes.
6. Resumen y preguntas de comprobación.
7. Ejercicio de aplicación o enlace explícito a uno.
8. Fuentes o documentación oficial cuando el producto o la técnica puedan cambiar.

Los diagramas se escriben dentro de la lección con Mermaid y se generan también en el PDF. `recursos/` solo contiene material complementario: nunca será el único lugar donde se explique un diagrama necesario.

## Estructura curricular

| Bloque | Lecciones previstas | Competencia de salida |
| --- | ---: | --- |
| 00. Orientación | 3 | Convertir una necesidad de negocio en una pregunta analítica. |
| 01. Fundamentos de datos | 4 | Entender grano, tipos, calidad, privacidad y fuentes. |
| 02. Python | 6 | Escribir, leer y depurar código básico reproducible. |
| 03. Matemáticas aplicadas | 4 | Interpretar magnitudes, tasas, funciones y comparaciones. |
| 04. NumPy | 3 | Pensar vectorialmente y manipular arrays numéricos. |
| 05. Pandas | 6 | Preparar y validar datos tabulares con trazabilidad. |
| 06. EDA | 4 | Investigar patrones y anomalías sin sobrerreclamar causalidad. |
| 07. Visualización | 4 | Elegir y diseñar gráficos que permitan decidir. |
| 08. Estadística | 6 | Comunicar incertidumbre y evaluar experimentos. |
| 09. SQL, NoSQL y almacenamiento | 7 | Consultar datos y entender su arquitectura y límites. |
| 10. Métricas y producto | 9 | Diseñar un sistema de métricas gobernado y accionable. |
| 11. Series temporales | 4 | Analizar evolución y evaluar previsiones base. |
| 12. Modelos predictivos | 5 | Aplicar predicción con validación, interpretación y ética. |
| 13. Herramientas y reproducibilidad | 6 | Entregar análisis colaborables y mantenibles. |
| 14. Nivel avanzado | 5 | Abordar causalidad, escala, anomalías y fuentes externas. |
| 15. Portfolio | 4 | Demostrar competencias mediante proyectos defendibles. |

Total: **80 lecciones**, que cubren los 161 temas del índice maestro.

## Mapa de lecciones por bloque

### 00. Orientación

1. Rol de analista, tipos de análisis y ciclo de decisión.
2. Preguntas, hipótesis, evidencia y métricas.
3. Herramientas, método de estudio y diagnóstico inicial.

### 01. Fundamentos de datos

1. Observaciones, variables, grano y tablas.
2. Tipos de datos, escalas y formatos.
3. Calidad, sesgo, privacidad y ética.
4. Relaciones, claves y lectura crítica de fuentes.

### 02. Python

1. Entorno, valores, variables y expresiones.
2. Colecciones y transformación de datos simples.
3. Condiciones, bucles y control de flujo.
4. Funciones, módulos y alcance.
5. Errores, depuración y pruebas mentales.
6. Estilo, legibilidad y práctica de gastos.

### 03-08. Núcleo analítico

- Matemáticas aplicadas: porcentajes y tasas; promedios ponderados; funciones; vectores y fechas.
- NumPy: arrays; selección; broadcasting y simulación.
- Pandas: importación; perfilado; selección; limpieza; agregación; uniones y validación.
- EDA: preguntas; distribuciones; segmentos; relaciones, outliers y registro de decisiones.
- Visualización: elección de gráfico; diseño honesto; Matplotlib/Seaborn; narrativa ejecutiva.
- Estadística: descriptiva; probabilidad; muestreo; incertidumbre; hipótesis; experimentos y tamaño de efecto.

### 09. SQL, NoSQL y almacenamiento

1. Modelo relacional, grano y SQL básico.
2. Agregaciones, joins y validación de cardinalidad.
3. CTE, subconsultas y funciones de ventana.
4. Fechas, nulos y consultas mantenibles.
5. MongoDB y agregaciones documentales.
6. DynamoDB y patrones de acceso.
7. Warehouse, lakehouse, extracción y consultas asistidas por AI.

### 10. Métricas y producto

1. Dato, medida, métrica, indicador y KPI.
2. Contrato de métrica: fórmula, población, grano, ventana, fuente y propietario.
3. Objetivos, North Star, árboles de métricas y guardrails.
4. Baselines, objetivos, benchmarks, ratios y comparaciones.
5. Funnel: definición, instrumentación y diagnóstico de conversión.
6. Cohortes, retención, churn y segmentación.
7. Métricas de adquisición, engagement, monetización y valor.
8. Experimentación, Goodhart y decisiones bajo incertidumbre.
9. Catálogo de métricas, tracking plan y Amplitude.

### 11-15. Consolidación profesional

- Series temporales: índices; componentes; lags; validación temporal y previsiones.
- Modelos predictivos: caso de uso; preparación; modelos; métricas; interpretación y sesgos.
- Herramientas: proyecto reproducible; Git; Jira; Amplitude; BI; documentación y entrega.
- Avanzado: causalidad; bootstrap; anomalías; escala; APIs, geoespacial y revisión crítica.
- Portfolio: selección de casos; narrativa; calidad; entrevistas; CV y capstone.

## Criterio de publicación

Un bloque solo se publicará como “desarrollado” cuando sus lecciones cubran todos los temas asignados en este documento. Un README de bloque será una puerta de entrada y una tabla de progreso, no la teoría completa.
