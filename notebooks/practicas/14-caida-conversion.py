"""Laboratorio reproducible del bloque 14.

No usa datos reales ni demuestra causalidad: muestra qué calcula un bootstrap
después de que el diseño y la calidad de medición se hayan definido.
"""

from random import Random
from math import sqrt


SEED = 14
N_PER_VARIANT = 4_000
REPLICAS = 2_000


def bernoulli_sample(random, probability, size):
    return [1 if random.random() < probability else 0 for _ in range(size)]


def proportion(values):
    return sum(values) / len(values)


def bootstrap_difference(random, a, b, replicas):
    """Remuestrea dentro de cada variante y devuelve diferencias B - A."""
    differences = []
    for _ in range(replicas):
        sample_a = [a[random.randrange(len(a))] for _ in a]
        sample_b = [b[random.randrange(len(b))] for _ in b]
        differences.append(proportion(sample_b) - proportion(sample_a))
    return sorted(differences)


def percentile(sorted_values, fraction):
    position = round((len(sorted_values) - 1) * fraction)
    return sorted_values[position]


def alert_should_fire(current_rate, comparable_rates, visits, minimum_visits=1_000):
    """Regla ilustrativa: 25 % bajo mediana comparable y volumen suficiente."""
    reference = sorted(comparable_rates)[len(comparable_rates) // 2]
    return visits >= minimum_visits and current_rate < reference * 0.75, reference


def main():
    random = Random(SEED)
    variant_a = bernoulli_sample(random, 0.048, N_PER_VARIANT)
    variant_b = bernoulli_sample(random, 0.040, N_PER_VARIANT)
    observed = proportion(variant_b) - proportion(variant_a)
    differences = bootstrap_difference(random, variant_a, variant_b, REPLICAS)

    print("Caso Lumen (simulado; no es evidencia causal)")
    print(f"A: {proportion(variant_a):.2%}; B: {proportion(variant_b):.2%}")
    print(f"Diferencia B - A: {observed:+.2%}")
    print(
        "Intervalo bootstrap percentil 95 %: "
        f"[{percentile(differences, 0.025):+.2%}, {percentile(differences, 0.975):+.2%}]"
    )

    fire, reference = alert_should_fire(
        current_rate=0.036,
        comparable_rates=[0.047, 0.049, 0.048, 0.050],
        visits=2_000,
    )
    print(f"Referencia estacional: {reference:.2%}; alerta: {fire}")
    print("Antes de escalar: comprobar frescura, evento booking_confirmed y despliegues.")


if __name__ == "__main__":
    main()
