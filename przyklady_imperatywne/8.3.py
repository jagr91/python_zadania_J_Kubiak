# Napisz program, który funkcję duze_litery() opakowuje inną funkcją,
# której argumentem jest inna funkcja. Do zamiany małych liter na duże
# litery wykorzystaj jej metodę upper().

def duze_litery(funkcja):
    def wrapper():
        tekst = funkcja()
        return tekst.upper()
    return wrapper


@duze_litery
def linia1():
    return 'Linia nr 1'


@duze_litery
def linia2():
    return 'Linia nr dwa'


def main():
    print(linia1())
    print(linia2())


if __name__ == '__main__':
    main()
