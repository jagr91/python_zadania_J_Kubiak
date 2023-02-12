# Napisz program, który na podstawie klasy z zadania 5.5 pokazuje mechanizm
# dziedziczenia

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


class Zatrudniony(Osoba):
    def __init__(self) -> None:
        print('Utowrzono nowy obiekt klasy Pracownik')

    def czytaj_dane1(self):
        self.departament = input('Podaj dział pracownika: ')

    def wyświetl_dane1(self):
        print(f'Adres: {self.departament}')


def main():
    Pracownik = Zatrudniony()
    Pracownik.czytaj_dane()
    Pracownik.czytaj_dane1()
    Pracownik.wyświetl_dane()
    Pracownik.wyświetl_dane1()


if __name__ == '__main__':
    main()
