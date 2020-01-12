import random

import battle
import parameters as params
from model import Team


def evolve():
    gen = 0
    population = init_population(params.all_pokemons, params.population_size)
    while gen < 49:
        sorted_population = battle.tournament(population)
        offspring = params.crossover(sorted_population)
        offspring = mutate(offspring)
        population = params.succession(sorted_population, offspring)
        gen += 1
    return sorted_population


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


winner = evolve()
