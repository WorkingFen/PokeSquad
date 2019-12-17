import random

from battle import tournament
from loader import load_pokemons

team_size = 6
all_pokemons = load_pokemons()


def evolve():
    crossover_prob = 0.5
    mutation_prob = 0.3
    population_size = 400
    parents_limit = int(400 * 0.6)
    elite_size = int(400 * 0.4)
    offspring_size = population_size - parents_limit
    population = initial_population(all_pokemons, population_size)
    while True:
        best_fits = selection(population, parents_limit)
        offspring = crossover(best_fits, offspring_size, crossover_prob)
        offspring = mutate(offspring, mutation_prob)
        population = pick_next_population(best_fits, offspring, elite_size)


def initial_population(pokemons: list, size: int):
    population = []
    for i in range(size):
        population.append(frozenset(random.choices(pokemons, k=team_size)))
    return population


def selection(population: list, limit: int):
    ranked_population = tournament(population)
    return ranked_population[:limit]


def crossover(best_fits: list, offspring_size: int, crossover_prob: float):
    offspring = []
    while len(offspring) < offspring_size:
        couple = random.choices(best_fits, k=2)
        if random.random() < crossover_prob:
            child = set()
            all_pokemons = [poke for parent in couple for poke in parent]
            while len(child) < team_size:
                for poke in all_pokemons:
                    if poke not in child and random.random() < 0.5:
                        child.add(poke)
            offspring.append(frozenset(child))
    return offspring


def mutate(offspring: list, probability: float):
    assert 0 <= probability <= 1
    mutants = []
    for team in offspring:
        mutated_team = []
        for pokemon in team:
            if random.uniform(0, 1) < probability:
                mutated_team.append(pokemon.mutant(all_pokemons))
            else:
                mutated_team.append(pokemon)
        mutants.append(frozenset(mutated_team))
    return mutants


def pick_next_population(best_fits: list, offspring: list, elite_size: int):
    return best_fits[:elite_size] + offspring


evolve()