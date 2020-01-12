def generative(sorted_population: list, offspring: list):
    # sorted population for argument consistency
    return offspring


def elite(sorted_population: list, offspring: list):
    from parameters import elite_limit, population_size
    assert len(sorted_population) >= elite_limit
    return sorted_population[:elite_limit] + offspring[:population_size - elite_limit]
