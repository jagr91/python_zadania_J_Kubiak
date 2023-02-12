# Napisz program, który rekurencyjnie znajduje 10 pierwszych liczb trójkątnych
# i wyświetla je na ekranie komputera

def licz_tro(n):
    if n == 1:
        return 1
    else:
        return n + licz_tro(n - 1)


def main():
    print('Program oblicza 10 pierwszych liczb trójkątnych:\n')
    for n in range(1, 11):
        print(f'{n} >> {licz_tro(n)}')


if __name__ == '__main__':
    main()
