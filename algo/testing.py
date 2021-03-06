import os
import statistics as stat
from collections import defaultdict

import matplotlib.pyplot as plt

import battle
import crossover
import main
import parameters as params
import replacement
import selection

if not os.path.exists('../data/plots'):
    os.mkdir('../data/plots')
if not os.path.exists('../data/results'):
    os.mkdir('../data/results')

test_selection = [selection.roulette, selection.ranked]
test_population = [params.small_population, params.big_population]
test_elite = [params.small_elite, params.big_elite]
test_ranked = [params.small_ranked_limit, params.big_ranked_limit]
test_cross_prob = [params.small_cross_prob, params.big_cross_prob]
test_dists = [params.norm_dist, params.local_dist, params.global_dist]
test_tournaments = [
    (battle.all_v_all, battle.random_pokemon),
    (battle.all_v_all, battle.first_pokemon),
    (battle.all_v_all_twice, battle.best_pokemon)
]
test_cross = [crossover.mixed, crossover.half_split]
test_succ = [replacement.elite, replacement.generative]

test_results = {}
for sel in test_selection:
    if sel is selection.ranked:
        for rank in test_ranked:
            test_name = f'test_main_{sel.__name__}_{rank}'
            total_results = defaultdict(list)
            for i in range(10):
                params.selection = selection.ranked
                params.population_size = 200
                params.elite_limit = 5
                params.ranked_limit = rank
                params.crossover_probability = 0.5
                params.mutation_dist = params.local_dist
                params.tournament_type = battle.all_v_all
                params.pokemon_selection = battle.first_pokemon
                params.crossover = crossover.half_split
                params.succession = replacement.elite
                results = main.evolve()
                for j in range(len(results)):
                    total_results[j].append(results[j])
            mean_scores = [stat.mean(v) for k, v in total_results.items()]
            test_results[f'{sel.__name__} {rank}'] = mean_scores
            with open(f'../data/results/{test_name}.csv', 'w') as f:
                for score in mean_scores:
                    f.write(f'{score}\n')
    else:
        test_name = f'test_main_{sel.__name__}'
        total_results = defaultdict(list)
        for i in range(10):
            params.selection = sel
            params.population_size = 200
            params.elite_limit = 5
            params.ranked_limit = 20
            params.crossover_probability = 0.5
            params.mutation_dist = params.local_dist
            params.tournament_type = battle.all_v_all
            params.pokemon_selection = battle.first_pokemon
            params.crossover = crossover.half_split
            params.succession = replacement.elite
            results = main.evolve()
            for j in range(len(results)):
                total_results[j].append(results[j])
        mean_scores = [stat.mean(v) for k, v in total_results.items()]
        test_results[f'{sel.__name__}'] = mean_scores
        with open(f'../data/results/{test_name}.csv', 'w') as f:
            for score in mean_scores:
                f.write(f'{score}\n')
for tested_obj, values in test_results.items():
    plt.plot(values, label=str(tested_obj))
plt.ylabel('mean score')
plt.xlabel('generation')
plt.legend()
plt.savefig(f'../data/plots/plot_main_test.png')
