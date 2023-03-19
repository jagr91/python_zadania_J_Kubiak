# Napisz program, który przedstawia klasę iteratora i rezultat jej działania

class Do_potęgi_2:
    def __init__(self, suma) -> None:
        self.suma = suma
        self.licznik = 0

    def __next__(self):
        self.licznik += 1
        return self.suma ** self.licznik


def main():
    potegowanie = Do_potęgi_2(50)

    print(next(potegowanie))
    print(next(potegowanie))
    print(next(potegowanie))
    print(next(potegowanie))


if __name__ == '__main__':
    main()
