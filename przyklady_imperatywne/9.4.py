# Napisz program demonstrujący różnicę między iteratorem a obiektem
# iterowalnym na przykładzie klasy Mnożenie_Przez_Dwa.

class Mnożenie_Przez_Dwa:
    def __init__(self, number, ograniczenie) -> None:
        self.number = number
        self.ograniczenie = ograniczenie
        self.licznik = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.licznik += 1
        wartosc = self.number * self.licznik

        if wartosc > self.ograniczenie:
            raise StopIteration
        else:
            return wartosc


def main():
    for number in Mnożenie_Przez_Dwa(200, 2000):
        print(number)


main()
