# Do zadania 4.5 wbuduj obsługę wyjątku na wypadek, gdyby a = 0.

from math import sqrt


def trojmian(a, b, c):
    delta = b * b - 4 * a * c

    print(f'Dla liczb:\na = {a}\nb = {b}\nc = {c}')

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

    try:
        trojmian(0, 2, 3)
    except ZeroDivisionError:
        print('\nBrak rozwiązania. Wartość a nie może być równa 0.')


if __name__ == '__main__':
    main()
