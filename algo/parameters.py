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
elite_limit = 10
crossover_probability = 0.5
mutation_probability = [0.05, 0.1, 0.35, 0.01, 0.04, 0.45]
optima = [200, 500, 1000, 2000, 4000, 5986, 9555, 11640, 17029]  # right -> better

# evolution
selection = selection.ranked
crossover = crossover.mixed
succession = replacement.elite


def reward(x):
    # ok >1150 > 650 > 1100 > 850
    # (x-350)^6 * (x-780)^4 * (x-920)^3 * (x-1000) * (x-1150)^2) / 10^20
    return -pow(x - 1150, 4) * (x - 1310) * pow(x - 1380, 2) * pow(x - 1520, 2) * pow(x - 1600, 2) * (x - 1650)

