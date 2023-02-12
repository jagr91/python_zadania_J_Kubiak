# Napisz program, który przechowuje dane pracownika w rekordzie, a następnie
# te rekordy zapisuje w pliku Pracownicy.txt

def main():
    liczba_rekordow = int(input('Podaj liczbę pracowników do dodania: '))
    path = (r'D:\G\OneDrive\G\Nauka\Python\Books\python - zadania z '
            r'programowania\przyklady_imperatywne\6.5_Pracownicy.txt')
    with open(path, 'w', encoding='utf-8') as plik:
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


if __name__ == '__main__':
    main()
