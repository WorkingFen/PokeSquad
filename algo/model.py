from enum import IntEnum
from random import choices

from aenum import Enum, NoAlias


class Pokemon(object):

    moves_count = 4

    def __init__(self, variant, name, hp, attack, defence, sp_attack, sp_defence,
                 speed, damage_multi: dict, occurrence, moves: list):
        self.__available_moves__ = moves
        self.variant = variant
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.sp_attack = sp_attack
        self.sp_defence = sp_defence
        self.speed = speed
        self.damage_multi = damage_multi
        self.occurrence = occurrence
        self.moves = choices(moves, k=Pokemon.moves_count)

    def mutant(self, pokemons):
        mutations = choices([0, 1, 2, 3, 4, 5], [0.05, 0.45, 0.35, 0.1, 0.04, 0.01], k=1)[0]
        if mutations == 5:
            return choices(pokemons, [p.occurrence for p in pokemons], k=1)[0]
        left = Pokemon.moves_count-mutations
        self.moves = choices(self.moves, k=left) + (choices(self.__available_moves__, k=mutations))
        return self


class Move(object):

    def __init__(self, type):
        self.type = type


class Type(IntEnum):
    NORMAL = 0
    FIRE = 1
    WATER = 2
    ELECTRIC = 3
    GRASS = 4
    ICE = 5
    FIGHT = 6
    POISON = 7
    GROUND = 8
    FLYING = 9
    PSYCHIC = 10
    BUG = 11
    ROCK = 12
    GHOST = 13
    DRAGON = 14
    DARK = 15
    STEEL = 16
    FAIRY = 17


class WeatherCondition(Enum, settings=NoAlias):
    CLEAR = 0.3
    SUN = 0.175
    RAIN = 0.175
    SANDSTORM = 0.125
    HAIL = 0.125
    FOG = 0.075
    SHADOWY_AURA = 0.025

    HEAVY_RAIN = 0
    WIND = 0
    EXTREME_SUN = 0

    @staticmethod
    def draw():
        conditions = [x for x in WeatherCondition if x.value > 0]
        return choices(conditions, [x.value for x in conditions], k=1)[0]
