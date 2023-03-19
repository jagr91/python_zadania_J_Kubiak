# Napisz program, który zawiera generator mnożący liczby

def generator_wielokrotny(liczba, limit):
    licznik = 1
    wartosc = liczba * licznik

    while wartosc <= limit:
        yield wartosc
        licznik += 1
        wartosc = liczba * licznik


def main():
    print('Generator mnożący liczby:')

    for liczba in generator_wielokrotny(300, 5000):
        print(liczba)


main()
