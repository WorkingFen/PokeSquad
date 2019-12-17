import random

from model import Pokemon
from model import WeatherCondition


def pokemon_battle(pokemon1: Pokemon, pokemon2: Pokemon):
    # TODO implement
    weather = WeatherCondition.draw()
    return random.choices([pokemon1, pokemon2], k=1)[0]


def team_battle(team1: list, team2: list):
    # TODO implement
    return random.choices([team1, team2], k=1)[0]


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
    print(f'best team score: {sorted_teams[0][1]}')
    return [x[0] for x in sorted_teams]
