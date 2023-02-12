# Napisz program, który za pomocą instrukcji for znajduje
# największą i najmniejszą liczbę ze zbioru n wylosowanych liczb całkowitych,
# generowanych losowo, w przedzoale od 0 do 100 (w zadaniu n = 5) oraz oblicza
# wartość średnią ze wszystkich wylosowanych liczb

from random import randint

n = 5
min = 100
max = 0
sum = 0

print('Wylosowane liczby to:')
for i in range(n):
    number = randint(0, 100)
    if number > max:
        max = number
    if number < min:
        min = number
    sum += number
    print(number, end=' ')

print(f'\nWartość minimalna to {min}')
print(f'Wartość maksymalna to {max}')
print(f'Średnia ze wszyttkich liczb to {sum / n:.2f}')
