# Napisz program, który korzystając z instrukcji while, sumuje
# liczby parzyste od 1 do 100

number = 1
sum = 0

while number <= 100:
    if number % 2 == 0:
        sum += number
        number += 1
    else:
        number += 1

print(f'Suma liczb parzystych od 1 do 100 to {sum}')
