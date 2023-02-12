# Napisz program, który tablicę 10x10 (poniżej) zapisuje do pliku
# tekstowego test.txt a następnie odczytuje ją z pliku i wyświetla na ekranie.
# Dodatkowo, po odczytaniu z pliku, program oblicza sumę liczb po przekątnej

# 1  0  0  0  0  0  0  0  0  0
# 0  1  0  0  0  0  0  0  0  0
# 0  0  1  0  0  0  0  0  0  0
# 0  0  0  1  0  0  0  0  0  0
# 0  0  0  0  1  0  0  0  0  0
# 0  0  0  0  0  1  0  0  0  0
# 0  0  0  0  0  0  1  0  0  0
# 0  0  0  0  0  0  0  1  0  0
# 0  0  0  0  0  0  0  0  1  0
# 0  0  0  0  0  0  0  0  0  1

def main():

    N = 10
    suma = 0
    path = (r'D:\G\OneDrive\G\Nauka\Python\Books\python - '
            r'zadania z programowania\przyklady_imperatywne\6.3_test.txt')
    tablica = [[i for i in range(N)] for i in range(N)]

    for wiersz in range(N):
        for poz in range(N):
            if wiersz == poz:
                tablica[wiersz][poz] = 1
            else:
                tablica[wiersz][poz] = 0

    with open(path, 'w') as plik:
        for wiersz in tablica:
            for poz in wiersz:
                plik.write(f'{poz}  ')
                suma += poz
            plik.write('\n')

    with open(path, 'r') as plik:
        for wiersz in plik.readlines():
            print(wiersz, end='')

    print(f'\nSuma liczb po przekątnej to {suma}')


if __name__ == '__main__':
    main()
