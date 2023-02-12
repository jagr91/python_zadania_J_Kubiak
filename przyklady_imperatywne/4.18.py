# Napisz program, który oblicza sumę wyrażenia:
# 1 + 2 - 3 + 4 - 5 + ... +- n dla dowolnego n

def oblicz(n):
    suma = 1
    for i in range(2, n + 1):
        if i % 2 == 0:
            suma = suma + i
        else:
            suma = suma - i
    return suma


def main():
    print('Program oblicza sumę z n = 100')
    print(oblicz(100))


if __name__ == '__main__':
    main()
