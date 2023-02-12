# Napisz program, który dla x rosnącego od 0 do 5 z krokiem 0,5 oblicza
# wartość funkcji y = x ** 2 + 1.
# Rozwiąż to zadanie, przekazując argument funkcji przez wartość

def oblicz(x):
    return x ** 2 + 1


def main():
    print('Program oblicza wartość funckji y = x ** 2 + 1, gdzie x <0, 5> i '
          'rośnie o 0.5:\n')
    x = 0
    krok = 0.5

    while x <= 5:
        print(f'x = {x:.2f},\ty = {oblicz(x):.2f}')
        x += krok


if __name__ == '__main__':
    main()
