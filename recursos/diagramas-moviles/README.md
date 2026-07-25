# Diagramas visibles en móvil

Esta carpeta contiene los SVG generados desde los bloques Mermaid de `curso/`.

La app móvil de GitHub puede mostrar el código Mermaid sin renderizarlo. Por eso cada lección enlaza a uno de estos SVG y conserva la fuente Mermaid plegada para que pueda editarse en GitHub web.

No editar los SVG a mano. Para regenerarlos tras añadir o cambiar un diagrama:

```powershell
python scripts/construir_diagramas_moviles.py
```

La comprobación de CI ejecuta `--check` y evita publicar una lección con Mermaid sin su fallback móvil.
