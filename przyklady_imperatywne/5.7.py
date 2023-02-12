# Zgodnie z zasadami programowania obiektowego, napisz program, który
# demonstruje przeciążanie metod. Program zawiera menu, które umożliwia
# obliczenie czterech pól: trójkąta, prostokąta, koła i trapezu.
# W programie należy utworzyć metodę oblicz_pole() w klasie o nazwie
# Pole_Figury. Następnie należy dokonać przeciążenia tej metody w czterech
# klasach dziedziczących o nazwach: Pole_Trójkąta, Pole_Prostokąta,
# Pole_Koła i Pole_Trapezu

class Pole_Figury():
    def __init__(self) -> None:
        print()

    def oblicz_pole():
        print()


class Pole_Trójkata(Pole_Figury):
    def __init__(self) -> None:
        print('\nOblicz Pole Trójkąta\n')

    def oblicz_pole(self):
        self.a = float(input("Podaj bok a: "))
        self.h = float(input("Podaj wysokość h: "))
        print(f'Pole trójkąta o boku a = {self.a} i podstawie h = {self.h} '
              f'wynosi {0.5 * self.a * self.h:.2f}')


class Pole_Prostokąta(Pole_Figury):
    def __init__(self) -> None:
        print('\nOblicz Pole Prostokąta\n')

    def oblicz_pole(self):
        self.a = float(input("Podaj bok a: "))
        self.b = float(input("Podaj bok b: "))
        print(f'Pole prostokąta o boku a = {self.a} i b = {self.b} wynosi '
              f'{self.a * self.b:.2f}')


class Pole_Koła(Pole_Figury):
    def __init__(self) -> None:
        print('\nOblicz Pole Koła\n')

    def oblicz_pole(self):
        from math import pi
        self.r = float(input("Podaj promień r: "))
        print(f'Pole koła o promieniu r = {self.r} wynosi '
              f'{pi * self.r ** 2:.2f}')


class Pole_Trapezu(Pole_Figury):
    def __init__(self) -> None:
        print('\nOblicz Pole Trapezu\n')

    def oblicz_pole(self):
        self.a = float(input("Podaj podstawę a: "))
        self.b = float(input("Podaj podstawę b: "))
        self.h = float(input("Podaj wysokość h: "))
        print(f'Pole Trapezu o podstawach a = {self.a} i b = {self.b} oraz '
              f'wysokości h = {self.h} wynosi '
              f'{(self.a + self.b) / 2 * self.h:.2f}')


def main():
    print('\nOblicz pole')
    print('1 - Trójkąta')
    print('2 - Prostokąta')
    print('3 - Koła')
    print('4 - Trapezu')

    choose = input('Wybierz odpowiedni numer aby obliczyć: ')

    if choose == '1':
        pole = Pole_Trójkata()
        pole.oblicz_pole()
    elif choose == '2':
        pole = Pole_Prostokąta()
        pole.oblicz_pole()
    elif choose == '3':
        pole = Pole_Koła()
        pole.oblicz_pole()
    elif choose == '4':
        pole = Pole_Trapezu()
        pole.oblicz_pole()
    else:
        print('Nie rozpoznano komendy. Spróbuj ponownie')


if __name__ == '__main__':
    main()
