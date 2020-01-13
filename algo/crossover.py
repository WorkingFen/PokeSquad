import random
import model


def prepare_pairs(sorted_population: list):
    from parameters import crossover_probability, selection
    pairs = []
    offspring = []
    while len(pairs) + len(offspring) < len(sorted_population):
        if random.random() < crossover_probability:
            pairs.append(tuple(selection(sorted_population, 2)))
        else:
            offspring.append(selection(sorted_population, 1)[0])
    return pairs, offspring


def half_split(population: list):
    from parameters import team_size
    pairs, offspring = prepare_pairs(population)
    for dad, mom in pairs:
        if random.random() < 0.5:
            child = list(list(dad.pokemons)[:int(team_size / 2)])
            for moms in reversed(list(mom.pokemons)):
                if len(child) < team_size:
                    child.append(moms)
                else:
                    break
        else:
            child = list(list(mom.pokemons)[:int(team_size / 2)])
            for dads in reversed(list(dad.pokemons)):
                if len(child) < team_size:
                    child.append(dads)
                else:
                    break
        won = int((dad.won_battles + mom.won_battles) / 2)
        lost = int((dad.lost_battles + mom.lost_battles) / 2)
        offspring.append(model.Team(child, won, lost))
    return offspring


def mixed(sorted_population: list):
    from parameters import team_size
    pairs, offspring = prepare_pairs(sorted_population)
    for dad, mom in pairs:
        child = []
        for dads in dad.pokemons:
            if random.random() < 0.5:
                child.append(dads)
        moms_sh = list(mom.pokemons)
        random.shuffle(moms_sh)
        for moms in moms_sh:
            if len(child) < team_size:
                child.append(moms)
            else:
                break
        won = int((dad.won_battles + mom.won_battles) / 2)
        lost = int((dad.lost_battles + mom.lost_battles) / 2)
        offspring.append(model.Team(child, won, lost))
    return offspring
