# Wiedząc, że 990100 = 990 ** 2 + 100 ** 2, napisz program , który znajduje
# liczby z przedziału od 100000 do 999999 spełniającą taką ciekawą zależność.
# Program dodatkowo liczy, ile ich jest

numbers = []

for i in range(100000, 1000000):
    f_number = i // 1000
    b_number = i % 1000
    if f_number * f_number + (b_number) * (b_number) == i:
        numbers.append(i)

print(f'Znaleziono {len(numbers)} liczbę:')
for i in numbers:
    print(f'{i} = {f_number} * {f_number} + {b_number} * {b_number}')
