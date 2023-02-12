# Napisz program, który za pomocą instrukcji while dla danych
# wartości x rosnących od 0 do 10 oblicza wartość funkcji y = 3x

print('Wartość funkcji y = 3x dla:')
x = 0
while x <= 10:
    print(f'x = {x}\ty = {3 * x}')
    x += 1
