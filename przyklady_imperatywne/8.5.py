# Napisz program, którym za pomocą menedżera kontekstu
# jest otwierany pilk i dokonywany jest zapis do pliku

class Do_pliku:
    def __init__(self, nazwa) -> None:
        self.nazwa = nazwa

    def __enter__(self):
        self.plik = open(self.nazwa, 'w', encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.plik:
            self.plik.close()

    def write(self, linia):
        self.plik.write(linia)


def main():
    with Do_pliku('8.5.txt') as p:
        p.write("Zapisywanie danych do pliku")
        p.write("Za pomocą menedżera kontekstu")
    print("Rezultat działania programu można zobaczyćw pliku o nazwie 8.5.txt")


if __name__ == '__main__':
    main()
