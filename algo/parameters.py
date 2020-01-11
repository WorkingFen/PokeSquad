import crossover
import loader as ldr
import replacement
import selection

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
mutation_probability = [0.05, 0.45, 0.35, 0.01, 0.04, 0.1]
optima = [200, 5986, 9555, 11640, 17029]  # right -> better

# evolution
selection = selection.roulette
crossover = crossover.mixed
succession = replacement.elite

