import random

import parameters as params


def list2pairs(l: list):
    it = iter(l)
    return list(zip(it, it))


def prepare_pairs(selected: list):
    shuffled_copy = selected[:]
    random.shuffle(selected[:])
    return list2pairs(shuffled_copy)


def half_split(selected: list):
    offspring = []
    pairs = prepare_pairs(selected)
    for dad, mom in pairs:
        if random.random() >= params.crossover_probability:
            offspring.append(dad)
            offspring.append(mom)
            continue
        if random.random() < 0.5:
            offspring.append(frozenset(dad[:params.team_size / 2] + mom[params.team_size / 2:]))
        else:
            offspring.append(frozenset(dad[params.team_size / 2:] + mom[:params.team_size / 2]))
    return offspring


def mixed(selected: list):
    offspring = []
    pairs = prepare_pairs(selected)
    for dad, mom in pairs:
        if random.random() >= params.crossover_probability:
            offspring.append(dad)
            offspring.append(mom)
            continue
        child = set()
        pokemons = list(dad) + list(mom)
        while len(child) < params.team_size:
            for poke in pokemons:
                if poke not in child and random.random() < 0.5:
                    child.add(poke)
        offspring.append(frozenset(child))
    return offspring
