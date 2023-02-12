# Samodzielnie zaprojektuj i napisz program w wersji obiektowej który zawiera
# obsługę prostej bazy damych opartej na rekordach, plikach tekstowych i
# funkcjonalnym menu. Temat bazy dowolny.

PLIK = (r'D:\G\OneDrive\G\Nauka\Python\Books\python - zadania z '
        r'programowania\przyklady_imperatywne\6.11_Baza.txt')


class Plik():

    def do_listy():
        lista = []
        with open(PLIK, 'r', encoding='utf-8') as plik:
            for linia in plik.readlines():
                # usuń znaki nowej linii i podziel po średniku
                linia = linia.strip().split(';')
                lista.append(linia)
        return lista

    def do_pliku(lista: list):
        for rekord in lista:
            # dodaj średniki do pliku
            rekord.insert(1, ';')
            rekord.insert(3, ';')
        with open(PLIK, 'w', encoding='utf-8') as plik:
            for rekord in lista:
                plik.writelines(rekord)
                if lista.index(rekord) + 1 != len(lista):
                    # nie dodawaj nowej linii na końcu
                    plik.write('\n')


class Dane():

    def przejrzyj():
        lista = Plik.do_listy()
        print('Lista zawodników:\n')
        for rekord in lista:
            print(f'Imię i nazwisko: {rekord[0]}')
            print(f'Rok urodzenia: {rekord[1]}')
            print(f'Klub: {rekord[2]}\n')

    def dodaj():
        lista = Plik.do_listy()
        liczba_rekordow = int(input('Podaj liczbę zawodników do dodania\n>> '))

        for i in range(liczba_rekordow):
            imie_nazwisko = input('Podaj imię i nazwisko\n>> ')
            rok_urodzenia = input('Podaj rok urodzenia\n>> ')
            klub = input('Podaj klub\n>> ')
            lista.append([imie_nazwisko, rok_urodzenia, klub])
        Plik.do_pliku(lista)
        print(f'Dodano zawodników w liczbie {liczba_rekordow}')

    def edytuj():
        lista = Plik.do_listy()
        dane = input('Podaj imię i nzawisko zawodnika do edycji\n>> ')
        for rekord in lista:
            if dane in rekord[0]:
                nowe_imie_nazwisko = input('Podaj nowe imię i nazwisko\n>> ')
                nowy_rok_urodzenia = input('Podaj nowy rok urodzenia\n>> ')
                nowy_klub = input('Podaj nowy klub\n>> ')
                rekord[0] = nowe_imie_nazwisko
                rekord[1] = nowy_rok_urodzenia
                rekord[2] = nowy_klub
        Plik.do_pliku(lista)
        print(f'Zmieniono zawodnika {dane}')

    def usun():
        lista = Plik.do_listy()
        dane = input('Podaj imię i nzawisko zawodnika do usunięcia\n>> ')
        for rekord in lista:
            if dane in rekord[0]:
                lista.remove(rekord)
        Plik.do_pliku(lista)
        print(f'Usunięto zawodnika {dane}')


def main():
    wybor = None

    while wybor != 'w':
        print('Witaj w bazie zawodników. Dostępne opcje:\n'
              '\n(p)rzejrzyj zawodników'
              '\n(d)odaj zawodników'
              '\n(e)dytuj zawodników'
              '\n(u)suń zawodników'
              '\n(w)yjdź')

        wybor = input('\n>> ').lower()
        if wybor == 'w':
            print('Do widzenia')
            exit()
        elif wybor == 'p':
            Dane.przejrzyj()
        elif wybor == 'd':
            Dane.dodaj()
        elif wybor == 'e':
            Dane.edytuj()
        elif wybor == 'u':
            Dane.usun()
        else:
            print('Nie rozpoznano komendy. Spróbuj ponownie')


if __name__ == '__main__':
    main()
