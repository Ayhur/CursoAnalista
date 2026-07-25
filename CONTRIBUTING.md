# Contribuir al curso

## Principios

- Escribe en español claro y define el vocabulario nuevo.
- Separa hechos, supuestos e interpretaciones.
- Incluye una fuente primaria cuando presentes una afirmación técnica que pueda cambiar.
- No uses datos personales ni credenciales en ejemplos.

## Añadir contenido

1. Crea o actualiza el Markdown del bloque en `curso/`.
2. Añade ejercicios solo cuando sirvan para practicar una competencia concreta.
3. Guarda las soluciones en la ruta equivalente bajo `soluciones/`.
4. Ejecuta `python scripts/construir_material.py --all`.
5. Comprueba los PDFs generados antes de publicar.

## PDFs

El script genera un PDF por bloque y un temario completo. Los archivos de `dist/` son derivados: no deben editarse manualmente.
