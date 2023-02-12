# Napisz zgodnie z zasadami programowania obiektowego program, który umieszcza
# na przekątnej tabliczy 10 x 10 liczby losowe od 0 do 9, a poza nią zera.
# Dodatkowo program oblicza sumę liczb znajdujących się na przekątnej.
# W programie skorzystaj z metod: zapelnij_tablice() i oblicz_sume().
# Pierwsza z nich wypełnia przekątną tablicy liczbami losowymi od 0 do 9.
# Druga oblicza sumę liczb na przekątnej.

import random


class Tablica():
    def __init__(self) -> None:
        print('Program umieszcza na przekątnej tablicy 10x10 losowe liczby z '
              'zakresu 0 do 9 oraz oblicza ich sumę')

    def zapelnij_tablice(self):
        self.sum = 0
        for line in range(10):
            print()
            for position in range(10):
                if line == position:
                    self.number = random.randint(0, 9)
                    self.oblicz_sume()
                    print(f'{self.number}  ', end="")
                else:
                    print('0  ', end="")

    def oblicz_sume(self):
        self.sum += self.number
        return self.sum


def main():
    tablica1 = Tablica()
    tablica1.zapelnij_tablice()
    print(f'\n\nSuma cyfr z przekątnej to: {tablica1.sum}')


if __name__ == '__main__':
    main()
