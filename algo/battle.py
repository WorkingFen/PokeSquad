import statistics as stat

import parameters as params
from logger import logger
from model import Category
from model import Move
from model import Pokemon
from model import Team
from model import Type


def tournament(teams: list):
    params.tournament_type(teams, team_battle)
    sorted_teams = sorted(teams, key=lambda p: -p.score())
    scores = [x.score() for x in teams]
    logger.info(
        f'size: {len(teams)}, '
        f'mean: {stat.mean(scores)}, '
        f'stddev: {stat.stdev(scores)}, '
        f'best: {sorted_teams[0].score()}, '
        f'won: {sorted_teams[0].won_battles}, '
        f'lost: {sorted_teams[0].lost_battles}, '
        f'diff: {sorted_teams[0].won_battles - sorted_teams[0].lost_battles}'
    )
    return sorted_teams


def pokemon_battle(friend: Pokemon, foe: Pokemon):
    friend_hp = (3 * friend.hp) + 15
    foe_hp = (3 * foe.hp) + 15
    friend_move = best_move(friend.moves, foe)
    foe_move = best_move(foe.moves, friend)
    friend_damage = max(get_damage(friend_move, friend, foe), 0.01)
    foe_damage = max(get_damage(foe_move, foe, friend), 0.01)
    if friend_hp / foe_damage >= foe_hp / friend_damage:
        foe.faint = True
    else:
        friend.faint = True


def team_battle(player_team: Team, opponent_team: Team):
    player_pokemons = list(player_team.pokemons.copy())
    opponent_pokemons = list(opponent_team.pokemons.copy())
    while len(player_pokemons) > 0 and len(opponent_pokemons) > 0:
        player_pokemon = params.pokemon_selection(player_pokemons, opponent_pokemons[0])
        pokemon_battle(player_pokemon, opponent_pokemons[0])
        if player_pokemon.faint:
            player_pokemons.remove(player_pokemon)
        else:
            opponent_pokemons.remove(opponent_pokemons[0])
    if len(player_pokemons) > 0:
        player_team.won_battles += 1
        opponent_team.lost_battles += 1
    else:
        player_team.lost_battles += 1
        opponent_team.won_battles += 1


def best_move(moves: list, pok: Pokemon):
    best = moves[0]
    best_value = 0
    for move in moves:
        value = move.power * pok.damage_multi[Type[move.type]]
        if best_value < value:
            best = move
            best_value = value

    return best


def get_damage(move: Move, friend: Pokemon, foe: Pokemon):
    if move.category is Category.SPECIAL:
        return ((2 * move.power * (friend.sp_attack / foe.sp_defense) / 25) + 2) * foe.damage_multi[Type[move.type]]
    else:
        return ((2 * move.power * (friend.attack / foe.defense) / 25) + 2) * foe.damage_multi[Type[move.type]]
