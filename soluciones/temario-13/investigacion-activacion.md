# Solución razonada - Investigación reproducible de activación

No hay una única redacción válida; esta solución ilustra el razonamiento y las comprobaciones que no pueden faltar.

## 1. Ticket y contrato

**Decisión:** el martes Producto decide limitar, corregir o revertir Android 4.2. **Pregunta:** para cuentas creadas entre el 1 y 28 de abril, ¿la proporción que crea una reserva confirmada en sus siete días siguientes difiere por plataforma y versión? **Corte:** 6 de mayo; así todas las altas del 28 de abril tienen siete días observables. **Exclusiones:** demos, cuentas internas y filas sin `account_id` válido.

La métrica es `cuentas activadas en 7 días / cuentas elegibles`, una fila por cuenta de alta. No es `eventos de reserva / eventos de alta`: una cuenta puede crear varias reservas y multiplicaría el numerador. Se registra UTC, fuente, versión `activation_v3` y dueños de Datos y Producto.

## 2. Tracking plan y control de calidad

`cuenta_creada` se emite cuando el backend confirma la cuenta con `account_id`, `timestamp_utc`, `platforma`, `version_app` y `canal`. `reserva_creada` se emite cuando el backend confirma una reserva con el mismo `account_id` y propiedades equivalentes. Ambos prohíben identificadores personales en la herramienta analítica.

El laboratorio simula que Android 4.2 tiene menos eventos `reserva_creada` reportados. La respuesta profesional no es «4.2 rompió el onboarding». Primero se compara cobertura de `reserva_creada` por día, plataforma y versión; se revisa el cambio de SDK/endpoint y se contrasta con una fuente transaccional. Si hay hueco de tracking, la tasa no mide comportamiento de manera comparable.

## 3. Estructura y cambios

```text
activacion-nebula/{README.md,docs/,src/,tests/,data/raw/,data/processed/,outputs/}
```

`data/raw/` y secretos se excluyen con `.gitignore`; se conserva una muestra sintética. Commits razonables: `Define contrato de activación a 7 días` y `Añade validación de cobertura por versión`. Un commit «arreglos» no permite revisar el propósito. Una PR debe pedir revisión de la definición de métrica y del manejo de duplicados, no solo que «pase el código».

## 4. Nota de decisión modelo

> Recomendamos no atribuir todavía la caída observada de activación Android a la versión 4.2 ni revertir basándonos solo en el funnel. El extracto muestra menor activación reportada en Android 4.2, pero la cobertura de `reserva_creada` cambia simultáneamente y puede ser una pérdida de instrumentación. Ingeniería validará la emisión servidor y corregirá el tracking si procede; Producto limitará el despliegue mientras tanto. Datos repetirá la cohorte con siete días completos el 13 de mayo. La decisión final se apoyará en tasa por cuenta, cobertura del evento y tamaños de grupo, no en eventos brutos.

La nota contiene acción, evidencia, incertidumbre, dueño y fecha. Cambiar «puede ser» por «es» sin validar la fuente sería una sobreafirmación.
