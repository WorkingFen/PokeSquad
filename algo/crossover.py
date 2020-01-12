import random

import model


def prepare_pairs(sorted_population: list):
    from parameters import crossover_probability, selection
    pairs = []
    offspring = []
    while len(pairs) + len(offspring) < len(sorted_population):
        if random.random() < crossover_probability:
            pairs.append(tuple(selection(sorted_population, 2)))
        else:
            offspring.append(selection(sorted_population, 1)[0])
    return pairs, offspring


def half_split(population: list):
    from parameters import team_size
    pairs, offspring = prepare_pairs(population)
    for dad, mom in pairs:
        if random.random() < 0.5:
            child = frozenset(list(dad.pokemons)[:int(team_size / 2)] + list(mom.pokemons)[int(team_size / 2):])
        else:
            child = frozenset(list(dad.pokemons)[int(team_size / 2):] + list(mom.pokemons)[:int(team_size / 2)])
        won = int((dad.won_battles + mom.won_battles) / 2)
        lost = int((dad.lost_battles + mom.lost_battles) / 2)
        offspring.append(model.Team(child, won, lost))
    return offspring


def mixed(sorted_population: list):
    pairs, offspring = prepare_pairs(sorted_population)
    for dad, mom in pairs:
        child = set()
        for dads, moms in zip(dad.pokemons, mom.pokemons):
            if random.random() < 0.5:
                child.add(dads)
            else:
                child.add(moms)
        won = int((dad.won_battles + mom.won_battles) / 2)
        lost = int((dad.lost_battles + mom.lost_battles) / 2)
        offspring.append(model.Team(frozenset(child), won, lost))
    return offspring
