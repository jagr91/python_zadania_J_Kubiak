# Napisz program, który rekurencyjnie oblicza wartości n! dla n = 10 i wynik
# wyświetla na ekranie komputera

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


def main():
    for n in range(0, 11):
        print(f'{n}! = {silnia(n)}')


if __name__ == '__main__':
    main()
