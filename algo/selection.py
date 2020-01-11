import random

import battle
import parameters as params


def roulette(population: list):
    selected = []
    ranked_population = battle.tournament(population)
    weights = [x[1] for x in ranked_population]
    ranked_population = [x[0] for x in ranked_population]
    # sum_score = functools.reduce(operator.add, [x[1] for x in ranked_population], 0)
    # while len(selected) < len(population):
    #     for team, score in ranked_population:
    #         if random.random() < score / sum_score:
    #             selected.append(team)
    return random.choices(ranked_population, weights=weights, k=len(population))


def ranked(population: list):
    ranked_population = battle.tournament(population)
    ranked_population = [x[0] for x in ranked_population[:params.ranked_limit]]
    return random.choices(ranked_population, k=len(population))

