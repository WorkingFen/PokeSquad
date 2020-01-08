import functools
import operator
import random

import battle
import parameters as params


def roulette(population):
    selected = []
    ranked_population = battle.tournament(population)
    sum_score = functools.reduce(operator.add, [x[1] for x in ranked_population], 0)
    for team, score in ranked_population:
        if random.random() < score / sum_score:
            selected.append(team)
    return population + selected


def ranked(population: list):
    ranked_population = battle.tournament(population)
    ranked_population = [x[0] for x in ranked_population]
    return population + ranked_population[:params.ranked_limit]

