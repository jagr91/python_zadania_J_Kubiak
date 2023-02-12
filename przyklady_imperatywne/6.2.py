# Zgodnie z zasadami programowania obiektowego (zob. zadanie 5.1)
# napisz program, który wczytuje z klawiatury imię i nazwisko, zapisuje te
# dane do pliku tekstowego test.txt a następnie odczytuje te dane z pliku
# i wyświetla je na ekranie komputera. Klasa powinna zawierać m.in. metody:
# __init__():
# zapisz_dane_do_pliku() - zapisuje dane do pliku tekstowego
# czytaj_dane_z_pliku() - odczytuje dane z pliku tekstowego
# i wyświetla na ekranie

path = (r'D:\G\OneDrive\G\Nauka\Python\Books\python - zadania z programowania'
        r'\przyklady_imperatywne\6.2_test.txt')


class Plik():

    def __init__(self) -> None:
        print('Utworzono obiekt klasy Plik')

    def zapisz_dane(self):
        self.dane = input('Podaj imię i nazwisko: ')

        with open(path, 'w') as file:
            file.write(self.dane)

    def wczytaj_dane(self):
        with open(path, 'r') as file:
            print(file.read())


def main():
    plik1 = Plik()
    plik1.zapisz_dane()
    plik1.wczytaj_dane()


if __name__ == '__main__':
    main()
