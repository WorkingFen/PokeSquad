import copy
import math
from enum import IntEnum
from random import choices
from random import sample


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

    def __repr__(self):
        return f'variant: {self.variant}, ' \
               f'name: {self.name}, ' \
               f'moves: {self.moves}'

    def mutate(self, all_pokemons, prob):
        mutant = copy.copy(self)
        mutations = choices([0, 1, 2, 3, 4, 5], prob)[0]
        if mutations == 5:
            return choices(all_pokemons, [p.occurrence for p in all_pokemons], k=1)[0]
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

    def __repr__(self):
        return f'name: {self.name}, ' \
               f'type: {self.type}, ' \
               f'category: {self.category}, ' \
               f'power: {self.power}'


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


class Team(object):

    def __init__(self, pokemons: frozenset, won=0, lost=0):
        assert len(pokemons) == 6
        self.pokemons = pokemons
        self.won_battles = won
        self.lost_battles = lost

    def __repr__(self):
        battles = self.won_battles + self.lost_battles
        score = self.won_battles / battles * (math.log(battles) + 1)
        return f'battles: {battles}, won: {self.won_battles}, lost: {self.lost_battles}, score: {score}'

    def score(self):
        battles = self.won_battles + self.lost_battles
        return self.won_battles / battles * (math.log(battles) + 1)

    def mutate(self, all_pokemons, prob):
        mutants = []
        for pokemon in self.pokemons:
            mutants.append(pokemon.mutate(all_pokemons, prob))
        assert len(mutants) == 6
        return Team(frozenset(mutants), self.won_battles, self.lost_battles)
