"""Laboratorio reproducible: lectura prudente de un experimento A/B.

Ejecución: python notebooks/practicas/08-experimento-onboarding.py
No requiere librerías externas. Los intervalos y p-valores son aproximaciones
normales didácticas; para decisiones de alto impacto usa revisión especializada.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path


DATA = Path(__file__).resolve().parents[2] / "datasets" / "experimentos" / "onboarding_nexo_agregado.csv"


def normal_cdf(value: float) -> float:
    return 0.5 * (1 + math.erf(value / math.sqrt(2)))


def load_totals() -> dict[str, dict[str, float]]:
    totals = {variant: {"asignados": 0, "expuestos": 0, "activados": 0,
                        "errores": 0, "cancelaciones_7d": 0, "p90_sum": 0,
                        "dias": 0} for variant in ("A", "B")}
    with DATA.open(encoding="utf-8", newline="") as source:
        for row in csv.DictReader(source):
            total = totals[row["variante"]]
            for key in ("asignados", "expuestos", "activados", "errores", "cancelaciones_7d"):
                total[key] += int(row[key])
            total["p90_sum"] += float(row["p90_carga_min"])
            total["dias"] += 1
    return totals


def main() -> None:
    totals = load_totals()
    a, b = totals["A"], totals["B"]
    p_a = a["activados"] / a["asignados"]
    p_b = b["activados"] / b["asignados"]
    difference = p_b - p_a
    se = math.sqrt(p_a * (1 - p_a) / a["asignados"] + p_b * (1 - p_b) / b["asignados"])
    low, high = difference - 1.96 * se, difference + 1.96 * se
    pooled = (a["activados"] + b["activados"]) / (a["asignados"] + b["asignados"])
    se_null = math.sqrt(pooled * (1 - pooled) * (1 / a["asignados"] + 1 / b["asignados"]))
    z = difference / se_null
    p_value = 2 * (1 - normal_cdf(abs(z)))

    print("Contrato: usuarios nuevos web ES; unidad=usuario; análisis ITT.")
    print(f"A: {a['activados']}/{a['asignados']} = {p_a:.2%}")
    print(f"B: {b['activados']}/{b['asignados']} = {p_b:.2%}")
    print(f"Diferencia B-A: {difference:.2%} ({difference * 100:.2f} pp); relativa: {difference / p_a:.1%}")
    print(f"IC 95% aproximado: [{low * 100:.2f}, {high * 100:.2f}] pp")
    print(f"z={z:.2f}; p-valor bilateral aproximado={p_value:.4f}")
    for variant, values in totals.items():
        print(f"{variant}: exposición={values['expuestos']/values['asignados']:.2%}, "
              f"errores={values['errores']/values['asignados']:.2%}, "
              f"p90 medio={values['p90_sum']/values['dias']:.2f} min, "
              f"cancelación={values['cancelaciones_7d']/values['asignados']:.2%}")
    print("\nInterpreta el resultado junto con el MDE (+1 pp), guardrails y calidad.")


if __name__ == "__main__":
    main()
