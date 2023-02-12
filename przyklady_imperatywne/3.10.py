# Liczbę pi można obliczać na wiele sposobów, np. metodą Monte Carlo. Napisz
# program, który oblicza liczbę pi z określoną dokładnością,
# korzystając z rysumku 3.10 i następującej listy kroków:
#   Wpisz koło o promieniu r w kwadrat o boku 2 * r
#   Losowo wygeneruj punkty i umieść je w kwadracie
#   Wyznacz liczbę punktów, które znajdują się jednocześnie w kwadracie i kole
#   Niech promień r będzie wyznaczony przez stosunek liczby punktóe
#   znajdujących się w kole do liczby punktów znajdujących się w kwadracie
# pi ~ 4.0 * r

import random
import math
from datetime import datetime

start = datetime.now()
print(f'Rozpoczęto obliczanie: {start}')

points = 100000
points_in_disk = 0

print(f'Liczba punktów: {points}')
print('Obliczam...')

for i in range(1, points):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    if x * x + y * y <= 1:
        points_in_disk += 1

stop = datetime.now()
calculated_pi = 4 * points_in_disk / points

print(f'Stała pi: {math.pi:.10f}')
print(f'Obliczone pi: {calculated_pi:.10f}')
print(f'Różnica: {calculated_pi - math.pi:.5f} / '
      f'{(calculated_pi - math.pi) / math.pi * 100:.3f}%')
print(f'Obliczono w czasie {stop - start} sekund')
