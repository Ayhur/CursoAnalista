# Protocolo de cátedra analítica

## Ámbito y obligatoriedad

Esta es una regla local de `CursoAnalista`. Se aplica **antes** de tocar un bloque, tema, lección, ejercicio, solución, notebook, diagrama, generador de PDF o material de evaluación. No sustituye `AGENTS.md`: lo concreta.

El objetivo es que cada cambio resista dos lecturas a la vez:

1. La de una persona que empieza y necesita una explicación gradual.
2. La de un catedrático o profesional de analítica que exige precisión, actualidad, aplicabilidad y límites explícitos.

No se permite ampliar contenido para aumentar páginas sin mejorar la comprensión o la capacidad de aplicar el conocimiento.

## Pasada previa obligatoria: diagnóstico catedrático

Antes de editar, leer como mínimo el README del bloque, todas sus lecciones, el ejercicio y solución asociados, y los documentos del programa que definan su competencia. Después contestar internamente —y dejarlo documentado si se abre una revisión amplia— estas preguntas:

1. **Propósito:** ¿qué decisión, problema de negocio o capacidad profesional permite resolver este bloque?
2. **Progresión:** ¿qué sabe ya Leo y qué términos técnicos nuevos deben enseñarse desde cero?
3. **Cobertura:** ¿faltan contexto, conceptos fundacionales, desarrollo técnico, contraejemplos, límites o conexiones con bloques anteriores/posteriores?
4. **Rigor:** ¿se distinguen observación, asociación, causalidad, predicción, estimación y decisión cuando procede?
5. **Actualidad:** ¿la práctica profesional ha sustituido, matizado o deprecado algún enfoque? Para productos, APIs, bibliotecas, estándares o reglas que cambian, verificar documentación primaria actual antes de afirmarlo.
6. **Aplicación:** ¿un alumno puede resolver un caso realista al terminar, o solo repetir definiciones?
7. **Evidencia:** ¿los ejercicios evalúan la competencia prometida y las soluciones explican el razonamiento, no solo la respuesta?
8. **Visuales:** ¿cada diagrama representa una relación real y se interpreta igual en GitHub y en el PDF?

Si alguna respuesta revela una carencia material, el cambio debe corregirla o declararla explícitamente como trabajo pendiente. No se marcará un bloque como desarrollado solo por tener archivos o títulos de lección.

## Diseño de una lección de nivel universitario-profesional

Toda lección nueva o revisada debe seguir esta secuencia, adaptada a la complejidad del tema:

1. Resultado observable y prerrequisitos reales.
2. Problema cotidiano o de negocio que el concepto ayuda a resolver.
3. Ejemplo mínimo visible **antes** de nombrar jerga técnica cuando el término sea nuevo.
4. Definición precisa, notación o sintaxis necesaria y supuestos.
5. Ejemplo trabajado dentro de la propia lección, preferiblemente continuo con un caso IT, producto u operaciones.
6. Interpretación: qué permite concluir y qué no.
7. Contraejemplo, error habitual, riesgo de calidad/sesgo/privacidad o límite operativo.
8. Relación con el siguiente concepto y práctica aplicable.

El caso práctico no se relegará al final como una frase decorativa. Debe intervenir durante la explicación para aclarar el significado de cada decisión técnica.

## Diagramas, ejemplos y PDF

- Todo diagrama responde una pregunta concreta, aparece junto a la explicación y lleva una interpretación posterior.
- La estructura visual debe ser semánticamente correcta. Relaciones paralelas se dibujan como ramas; secuencias como cadenas; alternativas como decisiones. Nunca aceptar que el renderizador convierta una relación de componentes en una secuencia falsa.
- Si el PDF simplifica Mermaid, adaptar el diagrama o el renderizador y revisar visualmente la página afectada.
- Todo código, tabla y ejemplo debe ser consistente con el texto y ejecutable o claramente marcado como pseudocódigo.

## Estándar específico: series temporales y previsión

Al crear o revisar material de series temporales, tratar estos elementos como lista de control obligatoria. Puede justificarse que alguno no aplica a un caso concreto, pero no omitirse por desconocimiento.

1. **Caso continuo completo:** por ejemplo, pedidos diarios de una app o comercio, desde carga, limpieza y calendario hasta una previsión que respalde una decisión.
2. **Contrato de previsión:** variable objetivo, unidad, frecuencia, granularidad, horizonte, fecha de corte, información disponible al predecir y decisión asociada.
3. **Calidad temporal:** zona horaria, duplicados, huecos, ceros frente a ausencia, agregación, cambios de definición y cobertura.
4. **Estructura temporal:** tendencia, estacionalidad semanal/anual, festivos/calendario, ciclos, ruido, cambios de nivel y rupturas; explicar componentes aditivos frente a multiplicativos cuando corresponda.
5. **Dependencia temporal:** lags, autocorrelación/ACF, medias y ventanas móviles; explicar qué información pasada entra en cada variable.
6. **Referencias comparables:** naïve, seasonal naïve, media móvil y al menos un modelo sencillo adicional adecuado al caso. Ningún modelo complejo se presenta sin superar una referencia honesta.
7. **Validación temporal:** train/validation/test en orden, walk-forward o expanding window, sin fuga de futuro; incluir un diagrama correcto de la partición.
8. **Evaluación:** MAE y RMSE; MAPE, sMAPE y MASE con sus limitaciones —en especial ceros y escalas—; seleccionar métrica según la decisión y el coste de error.
9. **Incertidumbre:** intervalos de predicción, calibración y comunicación de escenarios; nunca limitarse a escribir “± un margen”.
10. **Riesgos reales:** fugas de información con ejemplos, rupturas estructurales por precio, stock, campañas, tracking o cambios de producto, y plan de monitorización.
11. **Práctica verificable:** notebook o código reproducible, ejercicio aplicado con resultados esperados y solución razonada que explique decisiones y límites.

## Criterio de aceptación antes de publicar

Antes de publicar cambios de contenido:

1. Realizar la pasada de diagnóstico catedrático.
2. Comprobar que cada concepto técnico tiene escalón previo, ejemplo e interpretación.
3. Verificar actualidad con fuentes primarias cuando haya riesgo de obsolescencia.
4. Comprobar enlaces, ejercicios, soluciones y coherencia con `docs/programa-docente.md`.
5. Regenerar Markdown/PDF y extraer texto para comprobar presencia de las lecciones.
6. Renderizar y revisar visualmente las páginas modificadas, especialmente diagramas, tablas y código.
7. Comunicar con precisión qué se mejoró, qué se validó y qué sigue pendiente.

El incumplimiento de este protocolo bloquea declarar el material “desarrollado” o fusionarlo como revisión pedagógica terminada.
