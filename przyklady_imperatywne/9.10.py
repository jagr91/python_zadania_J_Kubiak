# Napisz program, który oblicza liczby pierwsze z przedziału 2 do 150 i
# umieszcza na liście o nazwie Lista. Do tego celu wykorzystaj generator
# tych liczb


def l_pierwsze(liczba):
    Lista = []
    for liczba in range(2, liczba):
        for i in Lista:
            if liczba % i == 0:
                break
        else:
            yield liczba
            Lista.append(liczba)


def main():
    lp = l_pierwsze(150)

    for i in lp:
        print(i)


if __name__ == '__main__':
    main()
