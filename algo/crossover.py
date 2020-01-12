import random

import parameters as params
from model import Team


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
            child = frozenset(dad.pokemons[:params.team_size / 2] + mom.pokemons[params.team_size / 2:])
        else:
            child = frozenset(dad.pokemons[params.team_size / 2:] + mom.pokemons[:params.team_size / 2])
        won = int((dad.won_battles + mom.won_battles) / 2)
        lost = int((dad.lost_battles + mom.lost_battles) / 2)
        offspring.append(Team(child, won, lost))
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
        offspring.append(Team(frozenset(child), won, lost))
    return offspring
