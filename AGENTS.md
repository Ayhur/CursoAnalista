# Reglas docentes de CursoAnalista

Estas reglas se aplican solo a este repositorio. El objetivo no es producir resúmenes: es construir un curso de análisis de datos aplicado a IT, adecuado para una persona principiante y suficientemente riguroso para servir como base de formación universitaria o de máster profesional.

## Protocolo obligatorio de cátedra analítica

**Antes de crear, modificar, revisar o publicar cualquier bloque, lección, ejercicio, solución, notebook, diagrama o PDF**, leer y aplicar el [Protocolo de cátedra analítica](docs/protocolo-catedra-analitica.md). Esta norma es exclusiva de `CursoAnalista`.

El protocolo exige una revisión docente y profesional previa, ejemplos prácticos integrados, contraste de actualidad cuando corresponda, práctica evaluable y validación semántica de diagramas. Para series temporales añade un estándar técnico específico: no se puede tratar como completo un bloque que omita los elementos aplicables de dicho estándar.

## Alumno de referencia: Leo

Asumir que Leo puede tener razonamiento matemático sólido, pero **no conoce todavía el vocabulario técnico de datos ni programación**. No se puede dar por sabido qué son:

- archivo, carpeta, tabla, fila, columna, celda, clave o relación;
- CSV, JSON, Excel, Parquet, base de datos, SQL, API o nube;
- variable, función, bucle, error, notebook o entorno de desarrollo;
- métrica, KPI, funnel, cohorte, retención o experimento.

Cada término nuevo debe aparecer en este orden:

1. Explicación en lenguaje cotidiano: qué problema resuelve.
2. Ejemplo visible y mínimo.
3. Nombre técnico y definición precisa.
4. Ejemplo aplicado a análisis de datos o a una empresa tecnológica.
5. Relación explícita con lo que se aprenderá después.

Nunca introducir una lista de tecnologías o siglas como si fuese autoexplicativa. CSV y JSON, por ejemplo, deben enseñarse mostrando primero qué es un archivo y cómo puede guardar información; no como un listado de formatos.

## Profundidad obligatoria

Un `README.md` de bloque es un índice y una visión general; **no es la teoría completa**. La teoría se divide en `lecciones/` y cada lección debe desarrollar una idea completa.

Antes de considerar una lección terminada, comprobar que contiene:

1. Objetivos de aprendizaje observables y prerrequisitos.
2. Explicación conceptual gradual, sin saltos de vocabulario.
3. Ejemplo trabajado, preferiblemente del ámbito IT, producto, negocio o datos reales simulados.
4. Contraejemplo, límite o error habitual.
5. Diagrama integrado cuando haya flujo, jerarquía, relación, arquitectura o decisión.
6. Resumen y preguntas de comprobación.
7. Ejercicio aplicado o enlace directo a un ejercicio.
8. Solución razonada cuando el ejercicio se publique.

Una lista de definiciones, tres párrafos breves o un único gráfico **no cumplen** este estándar.

## Diagramas y visuales

Los diagramas son parte de la explicación, no material decorativo ni un anexo en `recursos/`.

- Insertar el diagrama inmediatamente después de presentar la relación que aclara.
- Usar Mermaid para flujos, secuencias, arquitectura, árboles de métricas, relaciones y decisiones; el PDF debe mostrarlo de forma legible.
- Todo diagrama debe tener una frase anterior que formule la pregunta que responde y una posterior que interprete lo importante.
- No añadir diagramas genéricos que no enseñen nada nuevo.
- Si se utiliza una imagen externa, verificar licencia, atribución y URL de la fuente. Preferir diagramas originales en Mermaid para conceptos propios.

## Revisión pedagógica en dos pasadas

### Primera pasada: comprensión de cero

Leer la lección como alguien que no sabe qué es un CSV, JSON o tabla. Para cada término técnico preguntar: “¿se ha explicado antes, mostrado y usado con un ejemplo?”. Si no, añadir el escalón que falta.

### Segunda pasada: nivel profesional

Leer la lección como docente de analítica. Preguntar:

- ¿La definición es precisa y no induce una falsa intuición?
- ¿Se distinguen correlación, causalidad, observación e interpretación cuando procede?
- ¿El ejemplo permite tomar una decisión o solo ilustra sintaxis?
- ¿Se exponen límites, calidad de datos, sesgos, privacidad y riesgos cuando importan?
- ¿El contenido prepararía a alguien para justificar una decisión ante producto, ingeniería o dirección?

No publicar la lección si una de las dos pasadas falla.

## Arquitectura de contenido y PDF

- `curso/NN-nombre/README.md`: propósito, resultados, prerequisitos e índice de lecciones.
- `curso/NN-nombre/lecciones/`: desarrollo completo y ordenado de las unidades.
- `ejercicios/temario-NN/` y `soluciones/temario-NN/`: práctica y respuestas en rutas espejo.
- El generador de PDFs debe consolidar README y todas las lecciones del bloque en orden.
- No afirmar que un bloque o el curso está “completo” hasta cubrir todos los temas asignados en `docs/programa-docente.md`.

## Control de calidad antes de publicar

1. Comparar las lecciones del bloque con los temas asignados en `docs/programa-docente.md`.
2. Ejecutar `python scripts/construir_material.py --all`.
3. Revisar que el PDF del bloque contiene todas sus lecciones, no solo el índice.
4. Renderizar y revisar visualmente el PDF cuando haya diagramas, tablas o código.
5. Comprobar enlaces, ejercicios, soluciones y coherencia de vocabulario.
6. Describir honestamente qué está desarrollado, qué es índice y qué queda pendiente.
