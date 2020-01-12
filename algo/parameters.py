import crossover
import loader as ldr
import replacement
import selection

# constants
team_size = 6
all_pokemons = ldr.load_pokemons()

# parameters
population_size = 400
ranked_limit = 100
elite_limit = 10
crossover_probability = 0.5

# evolution
selection = selection.ranked
crossover = crossover.mixed
succession = replacement.elite

