import random

import parameters as params


def evolve():
    population = init_population(params.all_pokemons, params.population_size)
    while True:
        selected = params.selection(population)
        offspring = params.crossover(selected)
        offspring = mutate(offspring)
        population = params.succession(selected, offspring)


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
            mutated_team.append(pokemon.mutate(params.all_pokemons))
        mutants.append(frozenset(mutated_team))
    return mutants


evolve()