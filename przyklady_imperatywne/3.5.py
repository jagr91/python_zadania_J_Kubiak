# Napisz program, który za pomocą instrukcji while sumuje
# wszystkie liczby całkowite od 1 do 100.

number = 1
sum = 0

while number <= 100:
    sum += number
    number += 1

print(f'Suma liczb całkowitych od 1 do 100 to: {sum}')
