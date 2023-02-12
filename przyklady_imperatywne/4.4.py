# Napisz program, który definiuje i oblicza funkcję o nazwie
# trojka_pitagorejska (a, b, c) dla danych a, b i c wprowadzonych z klawiatury

def trojka_pitagorejska(a, b, c):
    if a * a + b * b == c * c:
        return True
    else:
        return False


def main():
    a = float(input('Podaj a:\n'))
    b = float(input('Podaj b:\n'))
    c = float(input('Podaj c:\n'))

    if trojka_pitagorejska(a, b, c):
        print(f'Liczby {a}, {b} i {c} tworzą trójkę pitagorejską,')
        print(f'bo {a} * {a} + {b} * {b} == {c} * {c}')
        print(f'{a * a} + {b * b} == {c * c}')
        print(f'{a * a + b * b} == {c * c}')
    else:
        print(f'Liczby {a}, {b} i {c} nie tworzą trójki pitagorejskiej,')
        print(f'bo {a} * {a} + {b} * {b} =/= {c} * {c}')
        print(f'{a * a} + {b * b} =/= {c * c}')
        print(f'{a * a + b * b} =/= {c * c}')


if __name__ == '__main__':
    main()
