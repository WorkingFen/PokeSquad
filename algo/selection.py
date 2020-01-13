import random


def roulette(sorted_population: list, k=1):
    weights = [x.score() for x in sorted_population]
    return random.choices(sorted_population, weights=weights, k=k)


def ranked(sorted_population: list, k=1):
    from parameters import ranked_limit
    population = sorted_population[:ranked_limit]
    return random.sample(population, k=k)
