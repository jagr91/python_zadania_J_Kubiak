# Zachęcam, abyś zgodnie z zasadami programowania obiektowego napisał program,
# który tablicę 10x10 (zob. zadanie 6.3) zapisuje do pliku tekstowego test.txt,
# a następnie z pliku tekstowego ją odczytuje i wyświetla na ekranie komputera.
# Dodatkowo, po odczytaniu tablicy z pliku, program powinien obliczać sumę
# liczb znajdujących się na przekątnej

path = (r'D:\G\OneDrive\G\Nauka\Python\Books\python - zadania z'
        r' programowania\przyklady_imperatywne\6.4_test.txt')


class Tablica():

    def zapisz_dane_do_pliku(self):

        N = 10
        self.suma = 0

        tablica = [[i for i in range(N)] for i in range(N)]

        for wiersz in range(N):
            for poz in range(N):
                if wiersz == poz:
                    tablica[wiersz][poz] = 1
                else:
                    tablica[wiersz][poz] = 0

        with open(path, 'w') as plik:
            for wiersz in tablica:
                for poz in wiersz:
                    plik.write(f'{poz}  ')
                    self.suma += poz
                plik.write('\n')

    def czytaj_dene_z_pliku(self):
        with open(path, 'r') as plik:
            for wiersz in plik.readlines():
                print(wiersz, end='')

        print(f'\nSuma liczb po przekątnej to {self.suma}')


def main():
    tablica1 = Tablica()
    tablica1.zapisz_dane_do_pliku()
    tablica1.czytaj_dene_z_pliku()


if __name__ == '__main__':
    main()
