import battle
import crossover
import loader as ldr
import replacement
import selection

# constants
team_size = 6
all_pokemons = ldr.load_pokemons()

norm_dist = [0.025, 0.1, 0.425, 0.375, 0.07, 0.005]
local_dist = [0.125, 0.375, 0.375, 0.1, 0.02, 0.005]
global_dist = [0.025, 0.05, 0.275, 0.325, 0.275, 0.05]

small_population = 50
big_population = 400

small_elite = 5
big_elite = 15

small_cross_prob = 0.1
big_cross_prob = 0.5

small_ranked_limit = 20
big_ranked_limit = 100


# parameters
population_size = 400
ranked_limit = 100
elite_limit = 10
crossover_probability = 0.5
tournament_type = battle.all_v_all
pokemon_selection = battle.random_pokemon
mutation_dist = norm_dist

selection = selection.ranked
crossover = crossover.mixed
succession = replacement.elite

