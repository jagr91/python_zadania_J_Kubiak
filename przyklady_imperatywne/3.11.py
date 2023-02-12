# Wiedząc, że 1233 = 12 ** 2 + 33 ** 2, napisz program , który znajduje
# wszystkie liczby z przedziału od 1000 do 9999 spełniającą taką
# ciekawą zależność.
# Program dodatkowo liczy, ile ich jest

numbers = []

for i in range(1000, 9999):
    x = int(str(i)[:2])
    y = int(str(i)[2:])
    if x * x + y * y == i:
        numbers.append(i)

print(f'Znalazłem {len(numbers)} takie liczby:')
for i in numbers:
    print(f'{int(str(i)[:2])} * {int(str(i)[:2])} + {int(str(i)[2:])} * '
          f'{int(str(i)[2:])} = {i}')
