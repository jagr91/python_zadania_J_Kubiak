# Napisz program, w którym zdefiniowano 4 funkcje: dodawanie, odejmowanie,
# mnożenie i dzielenie. Liczby a i b należy wprowadzić z klawiatury.
# Dodatkowo należy założyć, że b musi być różne od 0

def dodawanie(a, b):
    result = a + b
    return result


def odejmowanie(a, b):
    result = a - b
    return result


def mnozenie(a, b):
    result = a * b
    return result


def dzielenie(a, b):
    result = a / b
    return result


def main():
    a = float(input('Podaj a:\n'))
    b = float(input('Podaj b (różne od 0):\n'))

    if b == 0:
        print('Musisz podać b różne od 0')
    else:
        print(f'{a} + {b} = {dodawanie(a, b)}')
        print(f'{a} - {b} = {odejmowanie(a, b)}')
        print(f'{a} * {b} = {mnozenie(a, b)}')
        print(f'{a} / {b} = {dzielenie(a, b)}')


if __name__ == '__main__':
    main()
