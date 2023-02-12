# Napisz program, który pięciokrotnie wywołuje funkcję rekurencyjną

def wiadomosc(i):
    if i > 0:
        print('Wywołanie funkcji referencyjnej')
        wiadomosc(i - 1)


def main():
    wiadomosc(5)


if __name__ == '__main__':
    main()
