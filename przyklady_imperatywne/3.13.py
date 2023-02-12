# Napisz program, który znajduje liczby pierwsze z przedziału od 2 do 150

import math

liczby = []

for liczba in range(2, 151):
    if all(liczba % i != 0 for i in range(2, int(math.sqrt(liczba)) + 1)):
        liczby.append(liczba)

print(liczby)
