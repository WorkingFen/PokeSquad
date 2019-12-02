from model import Pokemon
from model import PokemonType


def load_pokemons():
    pokemon_list = []
    lines = open('data/Pokemon.csv').readlines()
    for line in lines[1:]:
        l = line.split(',')
        damage = {}
        for t in PokemonType:
            damage[t] = l[int(t) + 11]
        pokemon_list.append(Pokemon(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], damage, l[30], l[31], l[32], float(1/300)))
    return pokemon_list
