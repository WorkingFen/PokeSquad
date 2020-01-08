import loader as ldr


# constants
team_size = 6
all_pokemons = ldr.load_pokemons()
all_moves = ldr.load_moves()
all_abilities = ldr.load_abilities()

# parameters
population_size = 400
ranked_limit = 100
elite_limit = 50
crossover_probability = 0.5
mutation_probability = 0.3
