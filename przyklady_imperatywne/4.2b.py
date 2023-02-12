# Npisz program z prostym menu, w którym zdefiniowano cztery funkcje:
# dodawanie, odejmowanie, mnożenie i dzielenie.
# Funkcje te umieszczono w oddzielym pliku (module) Kalkulator.py. Program
# główny (poniżej) importuje moduł do programu.
# Liczby a i b należy wprowadzić z klawiatury. Dodatkowe trzeba założyć,
# że b jest różne do 0.

import Kalkulator


def numbers():
    a = float(input('Podaj a:\n'))
    b = float(input('Podaj b (różne od 0):\n'))
    return a, b


def calculation(function, f_name=str, sign=str):
    print(f'Wybrałeś {f_name}')
    a, b = numbers()
    print(f'{a} {sign} {b} = {function(a, b)}')


def main():
    print('''Witaj w kalkulatorze!
    Wybierz działanie, które chcesz wykonać:
    (d)odawanie
    (o)dejmowanie
    (m)nożenie
    (dz)ielenie\n''')

    menu_choose = input()

    if menu_choose == 'd':
        calculation(Kalkulator.dodawanie, 'dodawanie', '+')
    elif menu_choose == 'o':
        calculation(Kalkulator.odejmowanie, 'odejmowanie', '-')
    elif menu_choose == 'm':
        calculation(Kalkulator.mnozenie, 'mnożenie', '*')
    elif menu_choose == 'dz':
        calculation(Kalkulator.dzielenie, 'dzielenie', '/')
    else:
        print('Komenda nierozpoznana. Spróbuj ponownie.')


if __name__ == '__main__':
    main()
