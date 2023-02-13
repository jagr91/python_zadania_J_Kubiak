# Napisz program, który do pliku Pracownicy.txt dodaje nowe rekordy

def main():
    liczba_rekordow = int(input('Podaj liczbę pracowników do dodania: '))
    with open("6.5_Pracownicy.txt", 'w', encoding='utf-8') as plik:
        for pracownik in range(liczba_rekordow):
            imie_nazwisko = input(f'Podaj imię i nazwisko '
                                  f'({pracownik + 1}/{liczba_rekordow}): ')
            departament = input('Podaj departament: ')
            przelozony = input('Podaj imię i nazwisko przełożonego: ')
            if pracownik + 1 != liczba_rekordow:
                # nie dodawaj nowej linii po ostatnim rekordzie
                plik.writelines([imie_nazwisko, ';',
                                departament, ';', przelozony, '\n'])
            else:
                plik.writelines([imie_nazwisko, ';',
                                departament, ';', przelozony])

        print(f'Zapisano dane {liczba_rekordow} pracowników')

    kontynuuj = input('Czy chcesz dodać nowy rekord? (t/n) ').lower()
    while kontynuuj == 't':
        with open("6.5_Pracownicy.txt", 'a', encoding='utf-8') as plik:
            imie_nazwisko = input('Podaj imię i nazwisko: ')
            departament = input('Podaj departament: ')
            przelozony = input('Podaj imię i nazwisko przełożonego: ')
            plik.writelines(['\n', imie_nazwisko, ';', departament,
                             ';', przelozony])
            liczba_rekordow += 1
        print('Zapisano dane pracownika')
        kontynuuj = input('Czy chcesz dodać nowy rekord? (t/n) ')

    print(f'Zapisano dane {liczba_rekordow} pracowników')
    print('\nZakończono działanie programu')


if __name__ == '__main__':
    main()
