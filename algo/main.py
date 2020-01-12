import random

import battle
import crossover
import model
import parameters as params
import replacement
import selection
from logger import logger


def evolve():
    gen = 0
    population = init_population(params.all_pokemons, params.population_size)
    while gen < 250:
        sorted_population = battle.tournament(population)
        offspring = params.crossover(sorted_population)
        offspring = mutate(offspring)
        population = params.succession(sorted_population, offspring)
        gen += 1
    return battle.tournament(population)


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


test_selection = [selection.roulette]
test_population = [params.small_population, params.big_population]
test_elite = [params.small_elite, params.big_elite]
test_ranked = [params.big_ranked_limit]
test_cross_prob = [params.small_cross_prob, params.big_cross_prob]
test_dists = [params.norm_dist, params.local_dist, params.global_dist]
test_tournaments = [
    (battle.all_v_all, battle.random_pokemon),
    (battle.all_v_all, battle.first_pokemon),
    (battle.all_v_all_twice, battle.best_pokemon)
]
test_cross = [crossover.mixed, crossover.half_split]
test_succ = [replacement.elite, replacement.generative]

for sel in test_selection:
    for pop in test_population:
        for el in test_elite:
            for rank in test_ranked:
                for c_prob in test_cross_prob:
                    for dist in test_dists:
                        for t in test_tournaments:
                            for cross in test_cross:
                                for succ in test_succ:
                                    logger.info(f'starting test '
                                                f'selection: {sel.__name__}, '
                                                f'population: {pop}, '
                                                f'elite: {el}, '
                                                f'rank: {rank}, '
                                                f'crossover prob: {c_prob}, '
                                                f'mutation prob: {dist}, '
                                                f'tournament: {(t[0].__name__, t[1].__name__)}, '
                                                f'crossover: {cross.__name__}, '
                                                f'succession: {succ.__name__}')
                                    params.selection = sel
                                    params.population_size = pop
                                    params.elite_limit = el
                                    params.ranked_limit = rank
                                    params.crossover_probability = c_prob
                                    params.mutation_dist = dist
                                    params.tournament_type = t[0]
                                    params.pokemon_selection = t[1]
                                    params.crossover = cross
                                    params.succession = succ
                                    winner_population = evolve()
                                    logger.info(f'{winner_population[0]}, pokemons: {winner_population[0].pokemons}')
