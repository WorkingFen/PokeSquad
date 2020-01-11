import ast

import parameters as params
from model import Pokemon
from model import Move
# from model import Ability
from model import Type


def load_pokemons():
    pokemon_list = []
    lines = open('../data/pokemon.csv').readlines()
    for line in lines[1:]:
        attr = line.split(';')
        damage = {}
        variant = attr[1].upper() if len(attr[1]) > 0 else None
        name = attr[2].upper()
        # abilities = ast.literal_eval(attr[9])
        # abilities = [a.upper() for a in abilities]
        for t in Type:
            damage[t] = float(attr[int(t) + 10].replace(',', '.'))
        type1 = attr[29].upper()
        type2 = attr[30].upper()
        moves_names = ast.literal_eval(attr[37])
        moves_names = [m.upper() for m in moves_names]
        moves = [x for x in params.all_moves if x.name in moves_names]
        """
            hp = attr[3]
            attack = attr[4]
            defense = attr[5]
            sp_attack = attr[6]
            sp_defense = attr[7]
            speed = attr[8]
            occurrence = attr[36]
        """
        pokemon_list.append(
            Pokemon(variant, name, attr[3], attr[4], attr[5], attr[6], attr[7], attr[8],
                    # abilities,
                    damage, type1, type2, float(attr[36]), moves)
        )
    total_occurrence = sum([p.occurrence for p in pokemon_list])
    for p in pokemon_list:
        p.occurrence = p.occurrence / total_occurrence
    return pokemon_list


def load_moves():
    move_list = []
    lines = open('../data/move.csv').readlines()
    for line in lines[1:]:
        attr = line.split(';')
        name = attr[0].upper()
        type = attr[1].upper()
        category = attr[2].upper()
        # effects = ast.literal_eval(attr[8])
        # sec_effects = ast.literal_eval(attr[9])
        """
            power = attr[3]
            priority = attr[4]
            contact = attr[5]
            sound_type = attr[6]
            punch_type = attr[7]
        """
        move_list.append(
            Move(name, type, category, attr[3])
            # , attr[4], attr[5], attr[6], attr[7], effects, sec_effects)
        )
    return move_list


'''
def load_abilities():
    ability_list = []
    lines = open('../data/ability.csv').readlines()
    for line in lines[1:]:
        attr = line.split(';')
        name = attr[0].upper()
        effects = ast.literal_eval(attr[1])
        ability_list.append(Ability(name, effects))
    return ability_list
'''
