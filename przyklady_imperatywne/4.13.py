# Napisz program, który rekurencyjnie wyznacza największy wspólny dzielnik
# (NWD) dwóch liczb dodatnich x i y.
# NWD po angielsku oznacza the Greatest Common Divider (GCD)

def NWD(x, y):
    if x % y == 0:
        return y
    else:
        return NWD(y, x % y)


def main():
    print('Program po podaniu dwóch liczb dodatnich (a i b) oblicza najwyzszy '
          'wspólny dzielnik obu liczb\n')

    a = int(input('Podaj a:\n'))
    b = int(input('Podaj b:\n'))
    print(f'Największy wspólny dzielnik dla a = {a} i b = {b} to {NWD(a, b)}')


if __name__ == '__main__':
    main()
