import random

import parameters as params


def roulette(sorted_population: list, k=1):
    population = [x[0] for x in sorted_population]
    weights = [x[1] for x in sorted_population]
    return random.choices(population, weights=weights, k=k)


def ranked(sorted_population: list, k=1):
    population = [x[0] for x in sorted_population[:params.ranked_limit]]
    return random.choices(population, k=k)

