import random
import statistics as stat

import battle
import model
import parameters as params
from logger import logger


def evolve():
    generation = 0
    results = []
    logger.info(f'starting test '
                f'selection: {params.selection.__name__}, '
                f'population: {params.population_size}, '
                f'elite: {params.elite_limit}, '
                f'rank: {params.ranked_limit}, '
                f'crossover prob: {params.crossover_probability}, '
                f'mutation prob: {params.mutation_dist}, '
                f'tournament: {params.tournament_type.__name__}, '
                f'pokemon selection: {params.pokemon_selection.__name__}, '
                f'crossover: {params.crossover.__name__}, '
                f'succession: {params.succession.__name__}')
    population = init_population(params.all_pokemons, params.population_size)
    while generation < 100:
        sorted_population = battle.tournament(population)
        scores = [x.score() for x in sorted_population]
        mean = stat.mean(scores)
        stddev = stat.stdev(scores)
        best = sorted_population[0]
        logger.info(
            f'mean: {mean}, '
            f'stddev: {stddev}, '
            f'best: {best.score()}, '
            f'won: {best.won_battles}, '
            f'lost: {best.lost_battles}, '
            f'diff: {best.won_battles - best.lost_battles}'
        )
        results.append(mean)
        offspring = params.crossover(sorted_population)
        offspring = mutate(offspring)
        population = params.succession(sorted_population, offspring)
        generation += 1
    logger.info(f'{sorted_population[0]}, pokemons: {sorted_population[0].pokemons}')
    return results


def init_population(pokemons: list, size: int):
    population = []
    while len(population) < size:
        population.append(model.Team(random.choices(pokemons, k=params.team_size)))
    return population


def mutate(offspring: list):
    mutants = []
    for team in offspring:
        mutants.append(team.mutate(params.all_pokemons, params.mutation_dist))
    return mutants

