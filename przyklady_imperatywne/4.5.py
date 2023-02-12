# Napisz zgodnie z zasadami programowania modularnego program, który oblicza
# pierwiastki równania kwadratowego ax ** 2 + bx + c = 0 , gdzie
# zmienne a, b i c to liczby rzeczywiste. Dla zmiennych a, b, c, x1 oraz x2
# należy przyjąć format wyświetlania na ekranie z dokładnością do
# dwóch miejsc po kropce.

from math import sqrt


def trojmian(a, b, c):
    delta = b * b - 4 * a * c

    print(f'Dla liczb:\na = {a} b = {b} i c = {c}:')

    if delta < 0:
        print(f'Delta jest mniejsza od 0 ({delta}). Brak pierwiastków.')
    elif delta == 0:
        print(f'Delta równa 0. Pierwiastek z podanych liczb to {-b/(2*a)}')
    else:
        print(f'Delta powyżej 0. Rozwiązania równania to: '
              f'{(-b + sqrt(delta))/ (2 * a):.2f} i '
              f'{(-b - sqrt(delta))/ (2 * a):.2f}')


def main():
    print('Program oblicza pierwiatski równania kwadratowego y = ax2 + bx + c')
    print('Obliczanie Delty: b ** 2 - 4 * a * c')

    trojmian(-1, 2, 3)


if __name__ == '__main__':
    main()
