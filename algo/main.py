import random

import battle
import parameters as params
import multiprocessing
import time
from model import Team


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
        population.append(Team(random.choices(pokemons, k=params.team_size)))
    return population


def mutate(offspring: list):
    mutants = []
    for team in offspring:
        mutants.append(team.mutate(params.all_pokemons))
    return mutants


if __name__ == '__main__':
    process = multiprocessing.Process(target=evolve, name="Evolve")
    process.start()
    time.sleep(120)
    process.terminate()
    process.join()
