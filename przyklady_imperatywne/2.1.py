# Napisz program, który dla trzech liczb a, b i c wprowadzonych z klawiatury,
# sprawdza czy są to trójki pitagorejskie.
# Dodatkowo należy założyć, że a > 0, b > 0 i c > 0

a = int(input('Wprowadź a:\n>>>'))
b = int(input('Wprowadź b:\n>>>'))
c = int(input('Wprowadź c:\n>>>'))

if a > 0 and b > 0 and c > 0:
    if a * a + b * b == c * c:
        print(f'a = {a}, b = {b} i c = {c} tworzą trójkę pitagorejską.')
        print(f'{a * a + b * b} = {c * c}')
    else:
        print(f'a = {a}, b = {b} i c = {c} nie tworzy trójki pitagorejskiej')
        print(f'{a * a + b * b} =/= {c * c}')
else:
    print('Wprowadź liczby całkowite dodatnie')
