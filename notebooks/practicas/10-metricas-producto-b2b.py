"""Caso reproducible Lumen: métricas de producto B2B sin dependencias externas.

Ejecuta: python notebooks/practicas/10-metricas-producto-b2b.py
Los datos son sintéticos y pequeños para que se lea primero el razonamiento.
"""

from collections import defaultdict

EVENTS = [
    ("a01", 0, "workspace_created", "e01"), ("a01", 1, "source_connected", "e02"), ("a01", 2, "report_published", "e03"), ("a01", 25, "report_viewed_by_recipient", "e04"),
    ("a02", 0, "workspace_created", "e05"), ("a02", 2, "source_connected", "e06"), ("a02", 3, "report_published", "e07"), ("a02", 24, "report_published", "e08"),
    ("a03", 0, "workspace_created", "e09"), ("a03", 1, "source_connected", "e10"), ("a03", 30, "report_published", "e11"),
    ("a04", 0, "workspace_created", "e12"), ("a04", 1, "source_connected", "e13"), ("a04", 4, "report_published", "e14"), ("a04", 4, "report_published", "e14"),
    ("a05", 0, "workspace_created", "e15"), ("a05", 5, "report_published", "e16"),
    ("a06", 0, "workspace_created", "e17"), ("a06", 3, "source_connected", "e18"), ("a06", 7, "report_published", "e19"), ("a06", 23, "report_published", "e20"),
    ("a07", 0, "workspace_created", "e21"), ("a08", 0, "workspace_created", "e22"), ("a09", 0, "workspace_created", "e23"), ("a10", 0, "workspace_created", "e24"),
]

# Dedupe por idempotencia: un reintento del mismo evento no añade valor.
seen, clean = set(), []
for event in EVENTS:
    if event[3] not in seen:
        seen.add(event[3])
        clean.append(event)

by_account = defaultdict(list)
for account, day, name, _ in clean:
    by_account[account].append((day, name))

eligible = sorted(by_account)
connected = set()
activated = set()
returned_week4 = set()
for account, events in by_account.items():
    names_by_day = defaultdict(set)
    for day, name in events:
        names_by_day[day].add(name)
        if name == "source_connected" and day <= 14:
            connected.add(account)
    has_connection = any(name == "source_connected" and day <= 14 for day, name in events)
    has_publish_after_connection = any(
        name == "report_published" and day <= 14 and any(
            earlier_name == "source_connected" and earlier_day <= day
            for earlier_day, earlier_name in events
        )
        for day, name in events
    )
    if has_connection and has_publish_after_connection:
        activated.add(account)
    if any(name in {"report_published", "report_viewed_by_recipient"} and 22 <= day <= 28 for day, name in events):
        returned_week4.add(account)

def rate(part, whole):
    return f"{100 * part / whole:.1f}%" if whole else "n/a"

print(f"Cuentas elegibles: {len(eligible)}")
print(f"Conectaron fuente en 14d: {len(connected)} ({rate(len(connected), len(eligible))})")
print(f"Activadas en 14d: {len(activated)} ({rate(len(activated), len(eligible))})")
print(f"Retención S4 (cuentas activas semana 4): {len(returned_week4)} ({rate(len(returned_week4), len(eligible))})")
print(f"Duplicados descartados: {len(EVENTS) - len(clean)}")
print("Diagnóstico: el primer cuello de botella es conectar la fuente; no atribuyas todavía causalidad al editor.")
