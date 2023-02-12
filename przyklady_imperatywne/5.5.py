# Zgodnie z zasadami programowania obiektowego napisz program, który definiuje
# klasę Osoba i następujące maetody:
# czytaj_dane() i wyświetl_dane(). Metoda czytaj_dane() pozwala na
# wprowadzenie do programu takich danych jak nazwisko,
# imię i ulica. Metoda wyświetl_dane() wyprowadza na ekran monitora
# wprowadzone wcześniej dane nazwisko, imię i ulica.
# Na podstawie tak utworzonej klasy utwórz obiekt Pracownik

class Osoba:
    def __init__(self) -> None:
        print('Utowrzono nowy obiekt klasy Osoba')

    def czytaj_dane(self):
        self.nazwisko = input('Podaj nazwisko: ')
        self.imie = input('Podaj imię: ')
        self.ulica = input('Podaj adres: ')

    def wyświetl_dane(self):
        print(f'\nDane Pracownika {self.imie} {self.nazwisko}:')
        print(f'Imię: {self.imie}')
        print(f'Nazwisko: {self.nazwisko}')
        print(f'Adres: {self.ulica}')


def main():
    Pracownik = Osoba()
    Pracownik.czytaj_dane()
    Pracownik.wyświetl_dane()


if __name__ == '__main__':
    main()
