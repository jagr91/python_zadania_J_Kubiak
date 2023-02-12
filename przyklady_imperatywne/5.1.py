# Napisz zgodnie z zasadami programowania obiektowego program, który oblicza
# pole prostokąta. Klasa powinna zawierać m.in. trzy metody:
# czytaj_dane() - ta metoda umoźliwia wprowadzenie do programu wartości
# boków a i b z klawiatury. Należy przyjąć, że boki i zmienna pole są typu
# float
# przetworz_dane() - ta metoda oblicza pole prostokąta według wzoru
# pole = a * b
# wyswietl_wynik() - ta metoda wyświetla wartości boków a i b oraz zmiennej
# pole w określonym formacie

class Pole_prostokata():

    def __init__(self) -> None:
        print('\nProgram oblicza pole prostokąta a i b\n')
        print('Utworzono obiekt klasy Pole_prostokata')

    def czytaj_dane(self):
        self.a = float(input('Podaj bok a: '))
        self.b = float(input('Podaj bok b: '))

    def prztworz_dane(self):
        self.pole = self.a * self.b
        return self.pole

    def wyswietl_wynik(self):
        print(f'Pole prostokąta o boku a = {self.a} i b = {self.b} wynosi '
              f'{self.pole}')


def main():
    pole1 = Pole_prostokata()
    pole1.czytaj_dane()
    pole1.prztworz_dane()
    pole1.wyswietl_wynik()


if __name__ == '__main__':
    main()
