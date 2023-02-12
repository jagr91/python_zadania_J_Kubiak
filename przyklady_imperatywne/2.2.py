# Napisz program, który oblicza wartość x z równania ax + b = c.
# Wartości a, b i c należą do zbioru liczb rzczywistych i są wprowadzane
# z klawiatury. Dodatkowo należy zabezpieczyć program na wypadek sytuacji,
# kiedy wprowadzona wartość a jest równa zero. Dla zmiennych a, b i c oraz x
# należy przyjąć format wyświetlania ich z dokładnością do dwóch miejsc
# po kropce.

a = float(input('Podaj a (różne od 0):\n'))

if a == 0:
    print('Podałeś a = 0')
else:
    b = float(input('Podaj b:\n'))
    c = float(input('Podaj c:\n'))
    x = (a-b)/c
    print(f'\nx dla równania ax + b = c, gdzie a = {a:.2f}, b = {b:.2f}, '
          f'c = {b:.2f}, to {x:.2f}')
