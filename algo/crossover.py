import random

import parameters as params


def list2pairs(l: list):
    it = iter(l)
    return list(zip(it, it))


def prepare_pairs(sorted_population: list):
    pairs = []
    offspring = []
    while len(pairs) + len(offspring) < len(sorted_population):
        if random.random() < params.crossover_probability:
            pairs.append(tuple(params.selection(sorted_population, 2)))
        else:
            offspring.append(params.selection(sorted_population, 1)[0])
    return pairs, offspring


def half_split(population: list):
    pairs, offspring = prepare_pairs(population)
    for dad, mom in pairs:
        if random.random() < 0.5:
            offspring.append(frozenset(dad[:params.team_size / 2] + mom[params.team_size / 2:]))
        else:
            offspring.append(frozenset(dad[params.team_size / 2:] + mom[:params.team_size / 2]))
    return offspring


def mixed(sorted_population: list):
    pairs, offspring = prepare_pairs(sorted_population)
    for dad, mom in pairs:
        child = set()
        for dads, moms in zip(dad, mom):
            if random.random() < 0.5:
                child.add(dads)
            else:
                child.add(moms)
        offspring.append(frozenset(child))
    return offspring
