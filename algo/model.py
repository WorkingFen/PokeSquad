import copy
from enum import IntEnum
from random import choices
from random import sample

import parameters as params


class Pokemon(object):
    max_moves_count = 4

    def __init__(self, variant, name, hp, attack, defense, sp_attack, sp_defense,
                 speed, damage_multi: dict, type1, type2, occurrence: float, moves: list):
        self.__available_moves__ = moves
        self.variant = variant
        self.name = name
        self.hp = int(hp)
        self.attack = int(attack)
        self.defense = int(defense)
        self.sp_attack = int(sp_attack)
        self.sp_defense = int(sp_defense)
        self.speed = int(speed)
        self.damage_multi = damage_multi
        self.type1 = type1
        self.type2 = type2
        self.occurrence = occurrence
        self.moves = sample(moves, k=min(len(moves), Pokemon.max_moves_count))
        self.faint = False

    def mutate(self):
        mutant = copy.copy(self)
        mutations = choices([0, 1, 2, 3, 4, 5], params.mutation_probability)[0]
        if mutations == 5:
            return choices(params.all_pokemons, [p.occurrence for p in params.all_pokemons], k=1)[0]
        left = max(Pokemon.max_moves_count - mutations, 0)
        left_moves = sample(self.moves, k=min(left, len(self.moves)))
        new_moves = sample(self.__available_moves__, k=min(mutations, len(self.__available_moves__)))
        mutant.moves = left_moves + new_moves
        return mutant


class Move(object):

    def __init__(self, name, type, category, power):
        self.name = name
        self.type = type
        self.category = category
        self.power = int(power)


class Category(IntEnum):
    PHYSICAL = 0
    SPECIAL = 1
    OTHER = 2


class Type(IntEnum):
    NORMAL = 0
    FIRE = 1
    WATER = 2
    ELECTRIC = 3
    GRASS = 4
    ICE = 5
    FIGHTING = 6
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

