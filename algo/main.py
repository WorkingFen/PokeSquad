import random
import utils
from collections import defaultdict
from battle import tournament
from loader import load_pokemons

# constants
team_size = 6
all_pokemons = load_pokemons()

# parameters
selection_acceptance = 0.2  # [0.0 - 1.0]
elite_acceptance = 0.5
population_size = 400
crossover_probability = 0.5
mutation_probability = 0.3


def evolve():
    selection_limit = int(population_size * selection_acceptance)
    elite_limit = int(population_size * elite_acceptance)
    population = []
    while True:
        population = reproduce(population, all_pokemons, population_size)
        selected = selection(population, selection_limit)
        offspring = crossover(selected, crossover_probability)
        offspring = mutate(offspring, mutation_probability)
        population = next_population(selected, offspring, elite_limit, population_size, all_pokemons)


def reproduce(population: list, pokemons: list, size: int):
    while len(population) < size:
        population.append(frozenset(random.choices(pokemons, k=team_size)))
    return population


def selection(population: list, limit: int):
    selected = []
    prob = 1 / limit
    ranked_population = tournament(population)
    for team in ranked_population[:limit]:
        if random.random() < prob:
            selected.append(team)
    return selected


def crossover(selected: list, prob: float):
    offspring = []
    couples = utils.list2pairs(selected)
    for couple in couples:
        if random.random() >= prob:
            offspring.append(couple[0])
            offspring.append(couple[1])
            continue
        child = set()
        pokemons = list(couple[0]) + list(couple[1])
        while len(child) < team_size:
            for poke in pokemons:
                if poke not in child and random.random() < 0.5:
                    child.add(poke)
        offspring.append(frozenset(child))
    return offspring


def mutate(offspring: list, prob: float):
    mutants = []
    for team in offspring:
        mutated_team = []
        for pokemon in team:
            if random.random() < prob:
                mutated_team.append(pokemon.mutant(all_pokemons))
            else:
                mutated_team.append(pokemon)
        mutants.append(frozenset(mutated_team))
    return mutants


def next_population(best_fits: list, offspring: list, elite: int, size: int, pokemons: list):
    successors = (best_fits[:elite] + offspring)[:size]
    return successors[:size]
