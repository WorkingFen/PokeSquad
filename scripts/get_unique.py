import re


def make_unique(file):
    lst_tuple = []
    for line in file:
        lst_tuple += re.findall(r"'(.*?)'", line)
    return sorted(list(set([i for i in lst_tuple])))


def write_file(file, lst):
    for item in lst:
        file.write(item+"\n")


def get_unique_from_file():
    file = open("../data/non-duplicate_moves.json", "r", encoding="utf-8")
    save = open("../data/unique_moves.json", "a+", encoding="utf-8")
    new_line = make_unique(file)
    write_file(save, new_line)
    file.close()
    save.close()


get_unique_from_file()
