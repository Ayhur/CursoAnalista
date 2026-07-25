"""Laboratorio reproducible: visualización de un caso de producto.

Ejecuta: python notebooks/practicas/07-visualizacion-lumen.py
Requiere: pandas, matplotlib y seaborn. Crea PNGs en salidas/.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


OUTPUT = Path("salidas")
OUTPUT.mkdir(exist_ok=True)
sns.set_theme(style="whitegrid", context="notebook")

# Cada fila es un día y un canal, no una persona. Los datos son simulados.
rows = []
for day in range(1, 29):
    for channel, base_visits, base_rate in [
        ("Organic", 2200, 0.174), ("Paid", 1800, 0.145), ("Referral", 900, 0.188)
    ]:
        visits = base_visits + (day % 5) * 35
        # A partir de la versión 4.2 el 15, móvil pierde conversión.
        rate = base_rate - (0.030 if day >= 15 and channel == "Paid" else 0)
        checkout = round(visits * (0.225 if channel != "Paid" else 0.205))
        payments = round(visits * rate)
        rows.append((pd.Timestamp(2026, 5, day), channel, visits, checkout, payments))

daily = pd.DataFrame(rows, columns=["date", "channel", "visits", "checkout_start", "payment"])
assert (daily["visits"] > 0).all()
assert (daily["payment"] <= daily["checkout_start"]).all()
daily["conversion_pct"] = 100 * daily["payment"] / daily["visits"]

# 1. Evolución: agregado por día y anotación de contexto.
trend = daily.groupby("date", as_index=False)[["visits", "payment"]].sum()
trend["conversion_pct"] = 100 * trend["payment"] / trend["visits"]
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(trend["date"], trend["conversion_pct"], color="#2166ac", marker="o", ms=3)
ax.axvline(pd.Timestamp("2026-05-15"), color="#b2182b", ls="--", lw=1.5, label="Versión 4.2")
ax.annotate("Revisar caída y composición", xy=(trend.loc[17, "date"], trend.loc[17, "conversion_pct"]),
            xytext=(trend.loc[17, "date"], trend["conversion_pct"].max() + 0.25), arrowprops={"arrowstyle": "->"})
ax.set(title="Conversión diaria a pago — Lumen", xlabel="Fecha", ylabel="Pagos / visitas (%)")
ax.legend(frameon=False)
fig.autofmt_xdate()
fig.tight_layout()
fig.savefig(OUTPUT / "07-evolucion-conversion.png", dpi=160, bbox_inches="tight")
plt.close(fig)

# 2. Distribución: la variabilidad de la tasa diaria por canal.
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(data=daily, x="channel", y="conversion_pct", hue="channel", legend=False, palette="colorblind", ax=ax)
ax.set(title="Distribución diaria de conversión por canal", xlabel="Canal", ylabel="Pagos / visitas (%)")
fig.tight_layout()
fig.savefig(OUTPUT / "07-distribucion-segmentos.png", dpi=160, bbox_inches="tight")
plt.close(fig)

# 3. Segmentos: barras ordenadas; la tasa y el volumen se imprimen en tabla, no se mezclan en doble eje.
segment = daily.groupby("channel", as_index=False)[["visits", "payment"]].sum()
segment["conversion_pct"] = 100 * segment["payment"] / segment["visits"]
segment = segment.sort_values("conversion_pct")
fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.barh(segment["channel"], segment["conversion_pct"], color="#4dac26")
ax.bar_label(bars, labels=[f"{value:.1f}%" for value in segment["conversion_pct"]], padding=3)
ax.set(title="Conversión acumulada por canal", xlabel="Pagos / visitas (%)", ylabel="Canal", xlim=(0, 22))
fig.tight_layout()
fig.savefig(OUTPUT / "07-conversion-por-canal.png", dpi=160, bbox_inches="tight")
plt.close(fig)

# 4. Funnel: declara el paso de referencia.
totals = daily[["visits", "checkout_start", "payment"]].sum()
steps = pd.DataFrame({"step": ["Visita", "Inicio checkout", "Pago"], "count": totals.to_list()})
steps["pct_previous"] = 100 * steps["count"] / steps["count"].shift(fill_value=steps.loc[0, "count"])
fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.bar(steps["step"], steps["count"], color=["#1b9e77", "#7570b3", "#d95f02"])
ax.bar_label(bars, labels=[f"{n:,}\n{pct:.1f}% del paso previo" for n, pct in zip(steps["count"], steps["pct_previous"])], padding=3)
ax.set(title="Funnel de Lumen — mayo 2026", ylabel="Sesiones", ylim=(0, max(steps["count"]) * 1.18))
fig.tight_layout()
fig.savefig(OUTPUT / "07-funnel.png", dpi=160, bbox_inches="tight")
plt.close(fig)

print("Contrato: pago / visitas; grano día-canal; datos simulados.")
print(segment[["channel", "visits", "payment", "conversion_pct"]].to_string(index=False, formatters={"conversion_pct": "{:.2f}".format}))
print(f"Se han creado {len(list(OUTPUT.glob('07-*.png')))} gráficos en {OUTPUT.resolve()}")
