# Napisz program, który zapisuje dane: imię i nazwisko w pliku tekstowym
# test.txt a następnie odczytuje dane z pliku tekstowego i wyświetla na
# ekranie komputera. Wbuduj obsługę wyjątków na wypadek błędnej nazwy
# pliku do odczytu

def main():
    with open('7.3_test.txt', 'w') as plik:
        plik.write(input('Podaj imię i nazwisko do zapisu:\n>>'))

    nazwa_pliku = input('Podaj nazwę pliku do odczytu\n>>')

    try:
        with open(nazwa_pliku, 'r') as plik:
            print(plik.read())
    except FileNotFoundError:
        print('Nie znaleziono pliku o podanej nazwie')


if __name__ == '__main__':
    main()
