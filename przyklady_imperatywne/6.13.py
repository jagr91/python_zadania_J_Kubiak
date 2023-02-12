# Napisz program, który ilustruje zakładanie prostej bazy danych,
# wykorzystując mechanizm serializacj danych i menedżera kontekstu.

import pickle

PATH = (r'D:\G\OneDrive\G\Nauka\Python\Books\python - zadania z programowania'
        r'\przyklady_imperatywne\6.13')


def main():
    kraj = input('Podaj kraj\n>> ')
    nominal = input('Podaj nominał\n>> ')
    rok = input('Podaj rok\n>> ')

    dane_monety = [kraj, nominal, rok]

    with open(PATH, 'wb') as plik:
        pickle.dump(dane_monety, plik)

    with open(PATH, 'rb') as plik:
        dane = pickle.load(plik)

    print(dane)


main()
