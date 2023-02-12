# Na bazie zadania 5.5 napisz program, który wzbogacono o dodatkowe metody
# zapisz_dane_do_pliku() i czytaj_dane_z_pliku(self) umożliwiające zapis
# wprowadzanych danych do pliku i odczyt tych danych z pliku.

import pickle

PATH = (r'D:\G\OneDrive\G\Nauka\Python\Books\python - zadania z programowania'
        r'\przyklady_imperatywne\6.12')


class Osoba:
    def __init__(self) -> None:
        print('Utowrzono nowy obiekt klasy Osoba')

    def czytaj_dane(self):
        self.nazwisko = input('Podaj nazwisko: ')
        self.imie = input('Podaj imię: ')
        self.ulica = input('Podaj adres: ')
        self.dane = self.nazwisko + self.imie + self.ulica

    def zapisz_dane_do_pliku(self):
        with open(PATH, 'wb') as plik_zapis:
            pickle.dump(self.dane, plik_zapis)

    def czytaj_dane_z_pliku(self):
        with open(PATH, 'rb') as plik_oczyt:
            self.dane_plik = pickle.load(plik_oczyt)

    def wyświetl_dane(dane_plik):
        print(f'\nDane Pracownika {dane_plik.imie} {dane_plik.nazwisko}:')
        print(f'Imię: {dane_plik.imie}')
        print(f'Nazwisko: {dane_plik.nazwisko}')
        print(f'Adres: {dane_plik.ulica}')


def main():
    Pracownik = Osoba()
    Pracownik.czytaj_dane()
    Pracownik.zapisz_dane_do_pliku()
    print(f'Dane zapisano w {PATH}')
    Pracownik.czytaj_dane_z_pliku()
    print('Odczyt danych z pliku...')
    Pracownik.wyświetl_dane()


if __name__ == '__main__':
    main()
