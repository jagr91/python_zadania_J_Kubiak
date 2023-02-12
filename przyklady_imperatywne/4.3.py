# Napisz program, który dla danych a i b wprowadzonych z klawiatury oblicza
# pole prostokąta jako prostą funkcję

def pole_prostokata(a, b):
    return a * b


def main():
    print('By obliczyc pole prostokąta:')
    a = float(input('Podaj bok a\n'))
    b = float(input('Podaj bok b\n'))
    print(f'Pole prostokąta: {a} * {b} = {pole_prostokata(a,b)}')


if __name__ == '__main__':
    main()
