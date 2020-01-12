import random

import battle
import parameters as params
import multiprocessing
import time


def evolve():
    population = init_population(params.all_pokemons, params.population_size)
    while True:
        sorted_population = battle.tournament(population)
        offspring = params.crossover(sorted_population)
        offspring = mutate(offspring)
        population = params.succession(sorted_population, offspring)


def init_population(pokemons: list, size: int):
    population = []
    while len(population) < size:
        population.append(frozenset(random.choices(pokemons, k=params.team_size)))
    return population


def mutate(offspring: list):
    mutants = []
    for team in offspring:
        mutated_team = []
        for pokemon in team:
            mutated_team.append(pokemon.mutate())
        mutants.append(frozenset(mutated_team))
    return mutants


if __name__ == '__main__':
    process = multiprocessing.Process(target=evolve, name="Evolve")
    process.start()
    time.sleep(120)
    process.terminate()
    process.join()
