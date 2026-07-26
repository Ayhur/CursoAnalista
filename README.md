# Curso de Analista de Datos con Python

Curso abierto, en español y progresivo para aprender análisis de datos desde la base hasta nivel profesional. Está pensado para estudiar teoría desde el móvil y realizar las prácticas de código desde Google Colab o un ordenador.

## Empieza aquí

1. Lee la [guía de estudio](curso/00-orientacion/README.md).
2. Haz el [diagnóstico inicial](evaluaciones/diagnosticos/diagnostico-inicial.md).
3. Sigue los bloques en orden. Los apartados marcados como opcionales se pueden saltar si ya se dominan.
4. Intenta los ejercicios antes de mirar las soluciones.

## Descargas PDF

Los mismos contenidos se mantienen en Markdown y en PDF. Puedes descargar:

- [Temario completo consolidado en Markdown](dist/markdown/temario-completo.md)
- [Temario completo en PDF](dist/pdf/temario-completo.pdf)
- [Bloque 00 - Orientación](dist/pdf/00-orientacion.pdf)
- [Bloque 01 - Fundamentos de datos](dist/pdf/01-fundamentos-datos.pdf)
- [Bloque 02 - Python desde cero](dist/pdf/02-python-desde-cero.pdf)
- [Bloque 03 - Matemáticas aplicadas](dist/pdf/03-matematicas-aplicadas.pdf)
- [Bloque 04 - NumPy](dist/pdf/04-numpy.pdf)
- [Bloque 05 - Pandas](dist/pdf/05-pandas.pdf)
- [Bloque 06 - Análisis exploratorio](dist/pdf/06-analisis-exploratorio.pdf)
- [Bloque 07 - Visualización](dist/pdf/07-visualizacion.pdf)
- [Bloque 08 - Estadística](dist/pdf/08-estadistica.pdf)
- [Bloque 09 - SQL y NoSQL](dist/pdf/09-sql-nosql.pdf)
- [Bloque 10 - Métricas y producto](dist/pdf/10-metricas-y-producto.pdf)
- [Bloque 11 - Series temporales](dist/pdf/11-series-temporales.pdf)
- [Bloque 12 - Modelos predictivos](dist/pdf/12-modelos-predictivos.pdf)
- [Bloque 13 - Herramientas y reproducibilidad](dist/pdf/13-herramientas-y-reproducibilidad.pdf)
- [Bloque 14 - Nivel avanzado](dist/pdf/14-nivel-avanzado.pdf)
- [Bloque 15 - Portfolio](dist/pdf/15-portfolio.pdf)
- [Bloque 16 - Excel, Power Query y entrega automatizada](dist/pdf/16-excel-power-query-y-entrega.pdf)

Cada nuevo bloque añadirá su propio enlace. Los PDFs se regeneran con el script del repositorio y en GitHub Actions.

## Itinerario

| Bloque | Tema | Estado |
| --- | --- | --- |
| 00 | Orientación y pensamiento analítico | Desarrollado: 3 lecciones |
| 01 | Fundamentos de datos | Desarrollado: 4 lecciones |
| 02 | Python desde cero | Desarrollado: 6 lecciones |
| 03 | Matemáticas aplicadas (teoría general opcional) | Desarrollado: 6 lecciones |
| 04-09 | NumPy, Pandas, EDA, visualización, estadística y datos | Desarrollados: 34 lecciones |
| 10 | Métricas y producto | Desarrollado: 10 lecciones |
| 11-15 | Especialización y portfolio | Desarrollados: 29 lecciones |
| 16 | Excel, Power Query y entrega automatizada | En desarrollo: profesionalización aplicada |

## Cómo se organiza el material

- `curso/`: teoría en Markdown, un bloque por carpeta.
- `ejercicios/temario-XX/`: ejercicios asociados a cada bloque; solo se incluyen cuando aportan práctica real.
- `ejercicios/repaso-acumulativo/`: repasos espaciados de varios bloques.
- `soluciones/`: respuestas razonadas, con la misma ruta que el ejercicio.
- `evaluaciones/`: diagnósticos, pruebas de bloque, simulacros y rúbricas.
- `notebooks/`: prácticas para abrir en Google Colab.
- `dist/markdown/` y `dist/pdf/`: versiones consolidadas y descargables generadas.

## Diagramas

Los flujos de la teoría se escriben con Mermaid. Cada uno incluye además un SVG estático visible desde la app móvil de GitHub; en web se puede desplegar el código Mermaid editable. El generador de PDFs también los transforma en flujos visuales. Sirven para representar procesos, arquitectura de datos, decisiones y árboles de métricas, como los que se usan en documentación de equipos.

[Ver la guía de diagramas para empresa](recursos/diagramas-para-empresa.md).

## Estudiar desde móvil

La teoría, los ejercicios de razonamiento y las autoevaluaciones se pueden consultar desde el móvil. Para descargar un PDF en la app de GitHub, abre este `README`, entra en **Descargas PDF** y toca el enlace del bloque o del temario completo; después usa el menú de descarga o compartir del visor. Para programar, abre los notebooks en Colab; los proyectos largos son más cómodos desde ordenador.

[Abrir la primera práctica en Google Colab](https://colab.research.google.com/github/Ayhur/CursoAnalista/blob/main/notebooks/practicas/02-gastos-personales.ipynb)

## Aula interactiva beta

La carpeta [`web/`](web/README.md) contiene una primera aula estática: dos laboratorios autocorregibles, progreso guardado solo en el navegador y enlaces al Markdown fuente. Se puede abrir en local con `python -m http.server 8000 --directory web`; la publicación en GitHub Pages se añadirá tras validar el MVP.

## Herramientas que aprenderás a entender

Python, Pandas, SQL, MongoDB, DynamoDB, GitHub, Jira, Amplitude y herramientas BI. El objetivo no es memorizar una interfaz: primero se aprende el concepto de análisis y después cómo aplicarlo en cada herramienta.

## Estado del curso

Los 16 bloques originales están desarrollados como **92 lecciones**; el bloque 16 añade una primera experiencia profesional práctica. Se pueden leer en Markdown o descargar por bloque y como temario consolidado en PDF. Eso significa que la ruta conceptual está cubierta; no significa todavía que un alumno haya completado todas las experiencias prácticas propias de un puesto junior. La ampliación de Excel/Power Query, BI práctico, entregas automatizadas y casos empresariales se controla explícitamente en el [roadmap](ROADMAP.md). El criterio docente, la auditoría de reconstrucción y el mapa de cobertura están documentados en el [programa docente](docs/programa-docente.md) y la [auditoría docente](docs/auditoria-docente-2026-07.md).

## Licencia

El contenido se publica bajo licencia [MIT](LICENSE).
