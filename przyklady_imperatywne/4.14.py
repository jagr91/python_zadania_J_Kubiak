# Napisz program, który oblicza sumę wartości fragmentu elementów listy
# za pomocą rekurencji

def suma_zakresu(lista, poczatek, koniec):
    if poczatek > koniec:
        return 0
    else:
        return lista[poczatek] + suma_zakresu(lista, poczatek + 1, koniec)


def main():
    lista = [i for i in range(100)]
    print('Program oblicza sumę liczb z wycinka listy ')
    print(suma_zakresu(lista, 10, 30))


main()
