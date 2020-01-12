import ast

import model
from logger import logger


def load_pokemons():
    pokemon_list = []
    all_moves = load_moves()
    logger.info('loading pokemons')
    lines = open('../data/pokemon.csv').readlines()
    for line in lines[1:]:
        attr = line.split(';')
        damage = {}
        variant = attr[1].upper() if len(attr[1]) > 0 else None
        name = attr[2].upper()
        for t in model.Type:
            damage[t] = float(attr[int(t) + 10].replace(',', '.'))
        type1 = attr[29].upper()
        type2 = attr[30].upper()
        moves_names = ast.literal_eval(attr[37])
        moves_names = [m.upper() for m in moves_names]
        moves = [x for x in all_moves if x.name in moves_names]
        pokemon_list.append(
            model.Pokemon(variant, name, attr[3], attr[4], attr[5], attr[6], attr[7], attr[8],
                    damage, type1, type2, float(attr[36]), moves)
        )
    total_occurrence = sum([p.occurrence for p in pokemon_list])
    for p in pokemon_list:
        p.occurrence = p.occurrence / total_occurrence
    logger.info('pokemons loaded')
    return pokemon_list


def load_moves():
    move_list = []
    logger.info('loading moves')
    lines = open('../data/move.csv').readlines()
    for line in lines[1:]:
        attr = line.split(';')
        name = attr[0].upper()
        type = attr[1].upper()
        category = attr[2].upper()
        move_list.append(model.Move(name, type, category, attr[3]))
    logger.info('moves loaded')
    return move_list
