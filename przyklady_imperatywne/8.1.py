# Napisz program, który demonstruje użycie dekoratora, zamieniając małe
# litery w podanym ciągu na duże litery. Do zaminay wykorzystaj metodę
# upper().

def zamien_na_duze(inna_funkcja):
    tekst = inna_funkcja()
    # miejsce na inną funkcję (poprzez parametr w linii powyżej)
    return tekst.upper()


def main():
    @zamien_na_duze  # wykorzystanie funkcji zamien_na_duze
    def zwroc():  # funkja zwraca tekst do umieszczenia w linii nr 6
        return "To jest Tekst do zamiany na duże Litery"
    print(zwroc)


if __name__ == '__main__':
    main()
