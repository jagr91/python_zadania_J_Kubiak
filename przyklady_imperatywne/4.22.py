# Napisz program, który tworzy funkcję dodaj_do(), dodaje stałą do jej
# argumentu i zwracja jej wynik

def dodaj_do(x):
    def dodaj(y):
        return x + y
    return dodaj


def main():
    a = dodaj_do(15)
    print(a(10))


if __name__ == '__main__':
    main()
