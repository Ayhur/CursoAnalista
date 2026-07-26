# Aula web estática

Esta primera versión no duplica las lecciones: enlaza al Markdown del repositorio y aporta práctica autocorregible. No hay cuentas, servidor remoto ni ejecución arbitraria de código.

## Abrir en local

Desde la raíz del repositorio ejecuta:

```powershell
python -m http.server 8000 --directory web
```

Después abre `http://localhost:8000`. El progreso se guarda únicamente en `localStorage` del navegador. Los laboratorios con Python/SQLite siguen siendo los scripts del curso; el backend local opcional se incorporará solo cuando aporte valor didáctico real.
