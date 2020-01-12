import random

import parameters as params


def roulette(sorted_population: list, k=1):
    weights = [x.score() for x in sorted_population]
    return random.choices(sorted_population, weights=weights, k=k)


def ranked(sorted_population: list, k=1):
    population = sorted_population[:params.ranked_limit]
    return random.choices(population, k=k)
