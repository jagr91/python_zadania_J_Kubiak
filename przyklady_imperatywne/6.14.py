# Samodzielnie zaprojektuj i napisz program, który zawiera obsługę prostej
# bazy danych opartej na serializacji danych i funkcjonalnym menu.
# Temat dowolny.

import pickle


class Klub:

    def dodaj_klub():
        nazwa = input('\nPodaj nazwę klubu: ')
        utorzono = input('Podaj rok utworzenia: ')
        barwy = input('Podaj barwy: ')
        www = input('Podaj ares strony www: ')
        stadion = input('Podaj nazwe i adres stadionu: ')
        prezes = input('Podaj imię i nazwisko prezesa: ')
        trener = input('Podaj imię i nazwisko trenera: ')

        dane = [nazwa, utorzono, barwy, www,
                stadion, prezes, trener]

        return dane

    def dodaj_kluby():
        lista = Plik.plik_do_listy()
        l_klubow = int(input('Podaj liczbę klubów do dodania\n>>'))
        for i in range(l_klubow):
            klub = Klub.dodaj_klub()
            lista.append(klub)
        print(f'\nDodano klub(y) ({l_klubow}) do bazy.')
        return lista

    def edytuj_klub():
        lista = Plik.plik_do_listy()
        nazwa = input('Podaj nazwę klubu do zmiany: ').lower()
        for rekord in lista:
            if rekord[0].lower() == nazwa:
                indeks = lista.index(rekord)
                nowe_dane = Klub.dodaj_klub()
                lista[indeks] = nowe_dane
        print('\nEdycja zakończona sukcesem')
        return lista

    def usun_klub():
        lista = Plik.plik_do_listy()
        nazwa = input('Podaj nazwę klubu do zmiany: ')
        for rekord in lista:
            if rekord[0] == nazwa:
                lista.remove(rekord)
        print(f'\nUsunięto klub {nazwa}.')
        return lista


class Plik:

    def plik_do_listy():
        lista = []
        with open('6.14', 'rb') as plik:
            try:
                while True:
                    data = pickle.load(plik)
                    lista.append(data)
            except EOFError:
                pass
        return lista

    def do_bazy(lista):
        with open('6.14', 'wb') as plik:
            for rekord in lista:
                pickle.dump(rekord, plik)

    def czytaj_plik():
        print('Lista klubów:\n')
        rekord = ['Nazwa', 'Utorzono', 'Barwy', 'www', 'Stadion', 'Prezes',
                  'Trener']
        with open('6.14', 'rb') as plik:
            l_rekordow = 0
            try:
                while True:
                    dane_plik = pickle.load(plik)
                    for r, l in zip(rekord, dane_plik):
                        print(f'{r}: {l}')
                    l_rekordow += 1
                    print('\n')
            except EOFError:
                print(f'Koniec pliku. Łącznie rekordów: {l_rekordow}\n')


def main():
    wybor = None
    while wybor != 'z':

        print('Witaj w bazie danych klubów!\nDostępne opcje:\n')
        print('(l)ista klubów')
        print('(d)odaj klub/y')
        print('(e)dytuj klub')
        print('(u)suń klub')
        print('(z)amknij program')
        wybor = input('\n>>').lower()
        if wybor == 'z':
            print('Dziekujemy za skorzystane z programu!')
            print('Do zobaczenia!')
            exit()
        elif wybor == 'l':
            Plik.czytaj_plik()
        elif wybor == 'd':
            lista = Klub.dodaj_kluby()
            Plik.do_bazy(lista)
        elif wybor == 'e':
            lista = Klub.edytuj_klub()
            Plik.do_bazy(lista)
        elif wybor == 'u':
            lista = Klub.usun_klub()
            Plik.do_bazy(lista)
        else:
            print('Nie rozpoznano komendy. Spróbuj ponownie')


if __name__ == '__main__':
    main()
