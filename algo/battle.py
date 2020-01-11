import copy
import statistics

import parameters as params
from model import Pokemon
from model import Category
from model import Move
from model import Type

'''
def pokemon_battle(friend: Pokemon, foe: Pokemon):
    # TODO implement
    # weather = WeatherCondition.draw()
    return random.choices([friend, foe], k=1)[0]


def team_battle(team1: list, team2: list):
    # TODO implement
    # return random.choices([team1, team2], k=1)[0]
    team1_sum = sum([x.attack + x.defense for x in team1])
    team2_sum = sum([x.attack + x.defense for x in team2])
    return team1 if params.reward(team1_sum) > params.reward(team2_sum) else team2
'''


def tournament(teams: list):
    scores = {}
    for player_team in teams:
        for opponent_team in teams:
            if player_team is opponent_team:
                continue
            winner = team_battle(player_team, opponent_team)
            if player_team is winner:
                scores[player_team] = scores.get(player_team, 0) + 1
            else:
                scores[opponent_team] = scores.get(opponent_team, 0) + 1
    sorted_teams = sorted(scores.items(), key=lambda p: -params.reward(sum([x.attack + x.defense for x in p[0]])))
    data = []
    for team, score in sorted_teams:
        data.append(sum([x.attack + x.defense for x in team]))
    mean = statistics.mean(data)
    print(f'size: {len(teams)} mean: {mean}, best: {sum([x.attack + x.defense for x in sorted_teams[0][0]])}')
    return sorted_teams


def pokemon_battle(friend: Pokemon, foe: Pokemon):
    friend_hp = (3 * friend.hp) + 15    # HP = 3 * 'hp' + 15
    foe_hp = (3 * foe.hp) + 15
    # Abilities here?
    friend_move = best_move(friend.moves, foe)
    foe_move = best_move(foe.moves, friend)
    friend_damage = max(get_damage(friend_move, friend, foe), 0.01)
    foe_damage = max(get_damage(foe_move, foe, friend), 0.01)

    if friend_hp/foe_damage >= foe_hp/friend_damage:
        foe.faint = True
    else:
        friend.faint = True

    '''while tmp_friend.hp > 0 and tmp_foe.hp > 0:
        # friend_move = random.sample(tmp_friend.moves, k=1)
        # foes_move = random.sample(tmp_foe.moves, k=1)
        if tmp_friend.attack <= tmp_foe.defense and tmp_foe.attack <= tmp_friend.defense:
            tmp_foe.hp = -1
            break
        if tmp_friend.speed >= tmp_foe.speed:
            tmp_foe.hp -= max(tmp_friend.attack - tmp_foe.defense, 0)   # Damage = ((2 * 'power' * (A/D))/25 + 2) * Mod
            if tmp_foe.hp <= 0:
                continue
            tmp_friend.hp -= max(tmp_foe.attack - tmp_friend.defense, 0)
        else:
            tmp_friend.hp -= max(tmp_foe.attack - tmp_friend.defense, 0)
            if tmp_friend.hp <= 0:
                continue
            tmp_foe.hp -= max(tmp_friend.attack - tmp_foe.defense, 0)
    if tmp_friend.hp <= 0:
        friend.faint = True
    if tmp_foe.hp <= 0:
        foe.faint = True'''


def team_battle(player_team: list, opponent_team: list):
    player_pokemons = [x for x in player_team if not x.faint]
    opponent_pokemons = [x for x in opponent_team if not x.faint]
    while len(player_pokemons) > 0 and len(opponent_pokemons) > 0:
        player_pokemon = best_pokemon(player_pokemons, opponent_pokemons[0])
        pokemon_battle(player_pokemon, opponent_pokemons[0])
        if player_pokemon.faint:
            player_pokemons.remove(player_pokemon)
        else:
            opponent_pokemons.remove(opponent_pokemons[0])
        # player_pokemons = [x for x in player_team if not x.faint]
        # opponent_pokemons = [x for x in opponent_team if not x.faint]
    revive_team(player_team)
    revive_team(opponent_team)
    if len(player_pokemons) > 0:
        return player_team
    else:
        return opponent_team


def revive_team(team: list):
    for x in team:
        x.faint = False


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
