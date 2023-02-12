# Napisz program, który oblicza pierwiatki równania kwadratowego
# ax2 + bx + c = 0, gdzie znmienne a, b, c to liczby rzeczywiste
# wprowadzane z klawiatury. Dla zmiennych a, b, c, x1 i x2 należy przyjąć
# format wyświetlania ich na ekranie z dokładnością do dwóch miejsc po kropce

import math

print('Program oblicza pierwiatski równania kwadratowego y = ax2 + bx + c. '
      'Aby obliczyć pierwiastki:')

a = float(input('Podaj a:\n'))
b = float(input('Podaj b:\n'))
c = float(input('Podaj c:\n'))

delta = b * b - 4 * a * c

print('Obliczanie Delty: b * b - 4 * a * c')

if delta < 0:
    print(f'Delta jest niższa niż 0 ({delta}). Brak pierwiastków.')
elif delta == 0:
    print(f'Delta równa 0. Pierwiastek z podanych liczb to {-b/(2*a)}')
else:
    print(f'Delta powyżej 0. Rozwiązania równania to: '
          f'{(-b + math.sqrt(delta))/ (2 * a):.2f} i '
          f'{(-b - math.sqrt(delta))/ (2 * a):.2f}')
