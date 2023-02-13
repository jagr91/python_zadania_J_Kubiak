# Napisz program, który ilustruje zakładanie prostej bazy danych,
# wykorzystując mechanizm serializacj danych i menedżera kontekstu.

import pickle


def main():
    kraj = input('Podaj kraj\n>> ')
    nominal = input('Podaj nominał\n>> ')
    rok = input('Podaj rok\n>> ')

    dane_monety = [kraj, nominal, rok]

    with open('6.13', 'wb') as plik:
        pickle.dump(dane_monety, plik)

    with open('6.13', 'rb') as plik:
        dane = pickle.load(plik)

    print(dane)


if __name__ == '__main__':
    main()
