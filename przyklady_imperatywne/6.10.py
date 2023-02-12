# Samodzielnie zaprojektuj i napisz program, który zawiera obsługę
# prostej bazy damych opartej na rekordach, plikach tekstowych i
# funkcjonalnym menu. Temat bazy dowolny.

path = (r'D:\G\OneDrive\G\Nauka\Python\Books\python - zadania z '
        r'programowania\przyklady_imperatywne\6.10_Baza.txt')


def utworz_rekordy():
    l_rekordow = int(input('Podaj liczbę rekordów do dodania\n>>'))
    rekordy = []
    for rekord in range(l_rekordow):
        imie_nazwisko = input(f'Podaj imię i nazwisko({rekord + 1}/'
                              f'{l_rekordow})\n>> ')
        rok_urodzenia = input(f'Podaj rok urodzenia '
                              f'({rekord + 1}/{l_rekordow})\n>> ')
        klub = input(f'Podaj nazwę klubu ({rekord + 1}/{l_rekordow})\n>> ')
        rekord = [imie_nazwisko, ';', rok_urodzenia, ';', klub]
        rekordy.append(rekord)
    return rekordy


def plik_do_listy():
    with open(path, 'r', encoding='utf-8') as plik:
        lista = [line.split(';') for line in plik.readlines()]
        for rekord in lista:
            for item in rekord:
                if rekord.index(item) + 1 == len(rekord):
                    rekord[rekord.index(item)] = item.strip()
    return lista


def lista_do_pliku(lista: list):
    nowa_lista = []
    for rekord in lista:
        single_record = [rekord[0], ';', rekord[1], ';', rekord[2]]
        nowa_lista.append(single_record)

    with open(path, 'w', encoding='utf-8') as plik:
        for rekord in nowa_lista:
            if len(nowa_lista) == 1:
                for pole in rekord:
                    plik.writelines(pole)
            elif nowa_lista.index(rekord) + 1 != len(lista):
                for pole in rekord:
                    plik.writelines(pole)
                plik.write('\n')
            else:
                for pole in rekord:
                    plik.writelines(pole)


def dodaj_do_pliku(lista):
    with open(path, 'a', encoding='utf-8') as plik:
        plik.write('\n')
        for rekord in lista:
            if len(lista) == 1:
                for pole in rekord:
                    plik.writelines(pole)
            elif lista.index(rekord) + 1 != len(lista):
                for pole in rekord:
                    plik.writelines(pole)
                plik.write('\n')
            else:
                for pole in rekord:
                    plik.writelines(pole)


def czytaj_liste():
    lista = plik_do_listy()
    print('Lista zawodników:\n')
    for rekord in lista:
        print(f'Imię i Nazwisko: {rekord[0]} \nRok urodzenia: '
              f'{rekord[1]} \nKlub: {rekord[2]}\n')


def edytuj():
    lista = plik_do_listy()

    dane = input('Podaj imię i nazwisko do edycji:')
    for rekord in lista:
        if dane == rekord[0]:
            nowe_imie_nazwisko = input('Podaj nowe imię i nazwisko: ')
            nowy_rok_urodzenia = input('Podaj nowy rok urodzenia: ')
            nowy_klub = input('Podaj nowy klub: ')
            lista[lista.index(rekord)][0] = nowe_imie_nazwisko
            lista[lista.index(rekord)][1] = nowy_rok_urodzenia
            lista[lista.index(rekord)][2] = nowy_klub
            break
        else:
            print('Nie znaleziono zawodnika')
            break
    lista_do_pliku(lista)
    print(f'Zmieniono dane zawodnika {dane} ->> {nowe_imie_nazwisko}')


def usun():
    lista = plik_do_listy()
    dane = input('Podaj imię i nazwisko do usunięcia:')

    for rekord in lista:
        print(rekord[0])
        print(dane)
        if dane == rekord[0]:
            lista.remove(rekord)
            break
        else:
            print('Nie znaleziono zawodnika')
    lista_do_pliku(lista)
    print('Zawodnik usunięty\n')


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
            czytaj_liste()
        elif wybor == 'd':
            lista = utworz_rekordy()
            dodaj_do_pliku(lista)
        elif wybor == 'e':
            edytuj()
        elif wybor == 'u':
            usun()
        else:
            print('Nie rozpoznano komendy. Spróbuj ponownie')


if __name__ == '__main__':
    main()
