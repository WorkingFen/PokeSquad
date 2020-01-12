import parameters as params


def generative(sorted_population: list, offspring: list):
    # sorted population for argument consistency
    return offspring


def elite(sorted_population: list, offspring: list):
    assert len(sorted_population) >= params.elite_limit
    return sorted_population[:params.elite_limit] + offspring[:params.population_size - params.elite_limit]
