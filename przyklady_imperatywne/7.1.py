# Napisz program, w którym zdefiniowano cztery funkcje: dodawanie, odejmowanie,
# mnożenie i dzielenie. Liczby a i b należy wprowadzić z klawiatury
# (zob. zadanie 4.2). Wbuduj w program obsługę wyjątków na wypadek gdyby b = 0.

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

    try:
        print(f'{a} + {b} = {dodawanie(a, b)}')
        print(f'{a} - {b} = {odejmowanie(a, b)}')
        print(f'{a} * {b} = {mnozenie(a, b)}')
        print(f'{a} / {b} = {dzielenie(a, b)}')
    except ZeroDivisionError:
        print('Przy dzieleniu b nie może być równe 0')


if __name__ == '__main__':
    main()
