# Napisz program, który za pomocą instrukcji while wyświetla wszystkie
# liczby całkowite od 1 do 20.

start = 1

print('Liczby całkowite w przedziale od 1 do 20 to:')
while start <= 20:
    if start < 20:
        print(start, end=', ')
        start += 1
    else:
        print(start, end='.')
        start += 1
