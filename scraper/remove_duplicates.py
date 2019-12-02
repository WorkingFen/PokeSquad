import re


def remove_duplicates(lst):
    lst_tuple = re.findall(r"'(.*?)'", lst)
    return list(set([i for i in lst_tuple]))


def write_list(file, lst):
    file.write("[")
    for item in lst:
        if item != lst[-1]:
            file.write("'"+item+"', ")
        else:
            file.write("'"+item+"']\n")


def remove_from_file():
    file = open("moves.json", "r", encoding="utf-8")
    save = open("non-duplicate_moves.json", "a+", encoding="utf-8")
    for line in file:
        new_line = remove_duplicates(line)
        write_list(save, new_line)
    file.close()
    save.close()


remove_from_file()
