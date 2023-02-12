# Zgodnie z zasadami programowania obiektowego napisz program, który sortuje
# n liczb (w zadniu n = 6) znajdujących się na liście o nzawie
# liczby = [547, 303, -134, 125, 80, 236]. W zadaniu wykorzystaj
# algorytm sortowania bąbelkowego i stwórz metodę sortuj_dane()

class Sortuj():

    def __init__(self) -> None:
        print('\nProgram wykorzystuje sortowanie bąbelkowe do ułożenia listy '
              'liczb w kolejności od najmniejszej do największej')

    def sortuj_liczby(self, lista):
        for i in range(len(lista) - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    def wynik(self, lista):
        print(f'Posortowane liczby to {lista}')


def main():
    liczby = [547, 303, -134, 125, 80, 236]
    print(f'Nieposortowana lista to: {liczby}')
    s1 = Sortuj()
    s1.sortuj_liczby(liczby)
    s1.wynik(liczby)


if __name__ == '__main__':
    main()
