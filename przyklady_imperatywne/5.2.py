# Napisz zgodnie z zasadami programowania obiektowego program, który oblicza
# pierwiastki równania kwadratowego ax2 + bx + c, gdzie zmienne a, b i c to
# liczby rzeczywiste wprowadzane z klaiatury.
# Wyniki wyświetl z dokładnością do dwóch miejsc po kropce

import math


class Rownanie_kwadratowe():
    def __init__(self) -> None:
        print('Program oblicza pierwiatski równania kwadratowego '
              'y = ax\u00b2 + bx + c. Aby obliczyć pierwiastki:')

    def input_data(self):
        self.a = float(input('Podaj a: '))
        self.b = float(input('Podaj b: '))
        self.c = float(input('Podaj c: '))

    def calculate(self):
        print('\nObliczanie Delty: b\u00b2 - 4 * a * c')
        self.delta = self.b * self.b - 4 * self.a * self.c

    def print_result(self):
        print()
        if self.delta < 0:
            print(f'Delta jest niższa niż 0 ({self.delta}). '
                  'Brak pierwiastków.')
        elif self.delta == 0:
            print('Delta równa 0. Pierwiastek z podanych liczb to '
                  f'{-self.b/(2*self.a)}')
        else:
            print(f'Delta powyżej 0. Rozwiązania równania to: '
                  f'{(-self.b + math.sqrt(self.delta))/ (2 * self.a):.2f} i '
                  f'{(-self.b - math.sqrt(self.delta))/ (2 * self.a):.2f}')


def main():
    r1 = Rownanie_kwadratowe()
    r1.input_data()
    r1.calculate()
    r1.print_result()


if __name__ == '__main__':
    main()
