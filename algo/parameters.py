import random

import crossover
import loader as ldr
import replacement
import selection
from model import Pokemon
from model import Type


def all_v_all(teams: list, team_battle):
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            team_battle(teams[i], teams[j])


def all_v_all_twice(teams: list, team_battle):
    for player_team in teams:
        for opponent_team in teams:
            if player_team is opponent_team:
                continue
            team_battle(player_team, opponent_team)


def best_pokemon(team: list, foe: Pokemon):
    best = team[0]
    best_value = 4
    for pokemon in team:
        value = pokemon.damage_multi[Type[foe.type1]]
        if foe.type2:
            value += pokemon.damage_multi[Type[foe.type2]]
            value /= 2
        if best_value > value:
            best = pokemon
            best_value = value

    return best


def random_pokemon(team: list, *args):
    return random.choices(team)[0]


def first_pokemon(team: list, *args):
    return team[0]


# constants
team_size = 6
all_pokemons = ldr.load_pokemons()

# parameters
population_size = 400
ranked_limit = 100
elite_limit = 10
crossover_probability = 0.5
tournament_type = all_v_all
pokemon_selection = random_pokemon

# evolution
selection = selection.ranked
crossover = crossover.mixed
succession = replacement.elite

