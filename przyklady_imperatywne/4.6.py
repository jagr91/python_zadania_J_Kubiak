# Napisz program obliczjący funkcję signum dla dowolnej liczby rzeczywistej x

def signum(x):
    if x > 0:
        sin = 1
    elif x == 0:
        sin = 0
    else:
        sin = -1

    print(f'signum({x}) = {sin}')


def main():
    print('Program oblicza funkcję signum dla dowolnego x\n')

    signum(-123)
    signum(0)
    signum(2)


if __name__ == '__main__':
    main()
