# Napisz program, który demonstruje działanie nieskończonego iteratora next().

import itertools

lista = [0, 1, 2, 3]

iterator = itertools.cycle(lista)

for i in range(100):
    print(i, '-', next(iterator), end='|')
