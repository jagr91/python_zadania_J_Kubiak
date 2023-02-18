# Napisz program, który na bazie wcześniejszego programu ilustruje
# działanie kilku dekoratorów

def zamien_na_duze(inna_funkcja):
    tekst = inna_funkcja()
    # miejsce na inną funkcję (poprzez parametr w linii powyżej)
    return tekst.upper()


def main():
    @zamien_na_duze  # wykorzystanie funkcji zamien_na_duze
    def zwroc():  # funkja zwraca tekst do umieszczenia w linii nr 6
        return "To jest Tekst do zamiany na duże Litery"
    print(zwroc)

    @zamien_na_duze
    def zwroc2():
        return 'ooooooooooooooo - też duże. Funckja nr 2'
    print(zwroc2)

    @zamien_na_duze
    def zwroc3():
        return ('A to też jest tekst pisany dużymi literami. Tylko '
                'z innej funkcji')
    print(zwroc3)


if __name__ == '__main__':
    main()
