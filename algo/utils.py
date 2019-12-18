def list2pairs(l: list):
    it = iter(l)
    return list(zip(it, it))
