# Napisz program, który w odpowiednim przedziale czasu, tj. od 6.00 rano
# do 20.00, wyświetla określony komunikat

from datetime import datetime


def od_6_do_20(funkcja):
    def wrapper():
        if 6 <= datetime.now().hour < 20:
            funkcja()
        else:
            pass
    return wrapper


@od_6_do_20
def otwarte():
    print('Otwarte')


def main():
    otwarte()


if __name__ == '__main__':
    main()
