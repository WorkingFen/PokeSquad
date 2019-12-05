from model import Pokemon
from model import Type


def load_pokemons():
    pokemon_list = []
    lines = open('data/pokemon.csv').readlines()
    for line in lines[1:]:
        l = line.split(';')
        damage = {}
        variant = l[1] if len(l[1]) > 0 else None
        for t in Type:
            damage[t] = float(l[int(t) + 10])
        moves = l[37][1:][:-2].replace('\'', '').split(',')
        moves = [m.upper().strip() for m in moves]
        pokemon_list.append(Pokemon(variant, l[2], l[3], l[4], l[5], l[6], l[7], l[8], damage, float(l[36]), moves))
    total_occurrence = sum([p.occurrence for p in pokemon_list])
    for p in pokemon_list:
        p.occurrence = p.occurrence / total_occurrence
    return pokemon_list
