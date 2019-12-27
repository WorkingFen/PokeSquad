import random
import copy

from model import Pokemon
from model import WeatherCondition


'''
def pokemon_battle(friend: Pokemon, foe: Pokemon):
    # TODO implement
    # weather = WeatherCondition.draw()
    return random.choices([friend, foe], k=1)[0]


def team_battle(team1: list, team2: list):
    # TODO implement
    # return random.choices([team1, team2], k=1)[0]
    return team1 if sum([x.attack + x.defence for x in team1]) > sum([x.attack + x.defence for x in team2]) else team2
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
    sorted_teams = sorted(scores.items(), key=lambda p: -p[1])
    print(f'best team attack + defense: {sum([x.attack + x.defence for x in sorted_teams[0][0]])}')
    return [x[0] for x in sorted_teams]


def pokemon_battle(friend: Pokemon, foe: Pokemon):
    tmp_friend = copy.deepcopy(friend)
    tmp_foe = copy.deepcopy(foe)
    tmp_friend.hp = (3 * friend.hp) + 15    # HP = 3 * 'hp' + 15
    tmp_foe.hp = (3 * foe.hp) + 15
    # Abilities here?
    while tmp_friend.hp > 0 and tmp_foe.hp > 0:
        # friend_move = random.sample(tmp_friend.moves, k=1)
        # foes_move = random.sample(tmp_foe.moves, k=1)
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
        foe.faint = True


def team_battle(player_team: list, opponent_team: list):
    player_pokemons = [x for x in player_team if not x.faint]
    opponent_pokemons = [x for x in opponent_team if not x.faint]
    while len(player_pokemons) > 0 and len(opponent_pokemons) > 0:
        pokemon_battle(player_pokemons[0], opponent_pokemons[0])
        player_pokemons = [x for x in player_team if not x.faint]
        opponent_pokemons = [x for x in opponent_team if not x.faint]
    revive_team(player_team)
    revive_team(opponent_team)
    if len(player_pokemons) > 0:
        return player_team
    else:
        return opponent_team


def revive_team(team: list):
    for x in team:
        x.faint = False
