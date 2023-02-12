# Napisz program, który sortuje N liczb (w zadaniu N = 6) znajdujących się na
# liście o nazwie liczby

def sortuj(liczby):
    for i in range(len(liczby) - 1, 0, -1):
        for j in range(i):
            if liczby[j] > liczby[j + 1]:
                liczby[j], liczby[j + 1] = liczby[j + 1], liczby[j]


def main():
    liczby = [547, 303, -134, 125, 80, 236]
    print('Program sortuje listę liczb rosnąco')
    print(f'Lista liczb: {liczby}')
    sortuj(liczby)
    print(f'Lista posortowana: {liczby}')


if __name__ == '__main__':
    main()
