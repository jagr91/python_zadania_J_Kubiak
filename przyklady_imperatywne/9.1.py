# Napisz program, który pokazuje, że pętla for działa na dowolnym obiekcie,
# po którym można iterować. tymi obiektami są: lista o nazwie
# lista = [0, 1, 2, 3, 4, 5, 6], krotka o nazwie
# krotka = (1, 2, 3, 4, 5, 6) i łańcuch o nazwie łańcuch_znaków = 'Krzysztof'.

def main():
    lista = [0, 1, 2, 3, 4, 5, 6]
    krotka = (1, 2, 3, 4, 5, 6)
    łańcuch_znaków = 'Krzysztof'
    for i in lista:
        print(i, "|", end='')
    print('\n')
    for i in krotka:
        print(i, "|", end='')
    print('\n')
    for i in łańcuch_znaków:
        print(i, "|", end='')


if __name__ == '__main__':
    main()
