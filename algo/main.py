from loader import load_pokemons

import random


def evolve():
    crossover_prob = 0.5
    mutation_prob = 0.3
    population_size = 400
    all_pokemons = load_pokemons()
    population = initial_population(all_pokemons, population_size)
    while True:
        best_fits = selection(population)
        offspring = crossover(best_fits, crossover_prob)
        offspring = mutate(offspring, mutation_prob)
        population = pick_next_population(population, offspring)


def initial_population(pokemons: list, size: int):
    return random.choices(pokemons, k=size)


def selection(population: list):
    # selekcja turniejowa (?)
    return []


def crossover(best_fits: list, probability: float):
    return []


def mutate(offspring: list, probability: float):
    assert 0 <= probability <= 1
    mutants = []
    for pokemon in offspring:
        if random.uniform(0, 1) < probability:
            mutants.append(pokemon.mutant())
        else:
            mutants.append(pokemon)
    return mutants


def pick_next_population(parents: list, offspring: list):
    # sukcesja elitarna (?)
    return []

