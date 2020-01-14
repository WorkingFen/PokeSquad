import os
import re

import matplotlib.pyplot as plt


def create_plots():
    if not os.path.exists('../data/plots'):
        os.mkdir('../data/plots')
    tests = []
    log = open('../log/pokesquad.log').readlines()
    test = []
    for line in log:
        if line.startswith('starting') and len(test) > 0:
            tests.append(test)
        if line.startswith('starting'):
            title = [
                re.findall('selection: [^,]+', line)[0],
                re.findall('crossover: [^,]+', line)[0],
                re.findall('succession: [^\n]+', line)[0],
                re.findall('population: [^,]+', line)[0],
                re.findall('elite: [^,]+', line)[0],
                re.findall('crossover prob: [^,]+', line)[0],
                'distribution: normal' if '[0.025, 0.1, 0.425, 0.375, 0.07, 0.005]' in line else 'distribution: local',
            ]
            if 'random_pokemon' in line:
                title.append('tournament: random')
            elif 'first_pokemon' in line:
                title.append('tournament: first')
            else:
                title.append('tournament: best')
            test = [title]
        elif line.startswith('size'):
            values = re.findall('[0-9]+.?[0-9]+', line)
            test.append([float(x) for x in values])
    index = 1
    for test in tests:
        title_left = test[0][:4]
        title_right = test[0][4:]
        plt.figure(index)
        plt.plot([x[1] for x in test[1:]])
        plt.gca().set_position((.1, .3, .8, .6))
        plt.figtext(.10, .05, '\n'.join(title_left))
        plt.figtext(.40, .05, '\n'.join(title_right))
        plt.ylabel('mean score')
        plt.xlabel('generation')
        plt.savefig(f'../data/plots/plot_{"_".join(test[0])}.png')
        plt.close(index)
        index += 1


create_plots()