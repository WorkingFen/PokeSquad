from enum import IntEnum


class Pokemon(object):

    def __init__(self, number, variant, name, hp, attack, defence, sp_attack, sp_defence,
                 speed, damage_multi: dict, classification, type1, type2, occurrence, moves: list):
        self.number = number
        self.variant = variant
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.sp_attack = sp_attack
        self.sp_defence = sp_defence
        self.speed = speed
        self.damage_multi = damage_multi
        self.classification = classification
        self.type1 = type1
        self.type2 = type2
        self.occurrence = occurrence
        self.moves = moves

    def taken_hit(self, other):
        return self.damage_multi.get(other.type1, 1.0) * self.damage_multi.get(other.type2, 1.0)


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


class WeatherCondition(IntEnum):
    CLEAR = 0
    SUN = 1
    EXTREME_SUN = 2
    RAIN = 3
    HEAVY_RAIN = 4
    SANDSTORM = 5
    HAIL = 6
    SHADOWY_AURA = 7
    FOG = 8
    WIND = 9
