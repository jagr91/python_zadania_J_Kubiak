# Napisz program, ktory generuje 5 liczb pseudolosowych z przedziału
# od 1 do 100

from random import randint

print('Oto 5 liczb pseudolosowych:\n')
for i in range(5):
    liczba = randint(1, 100)
    print(liczba)
