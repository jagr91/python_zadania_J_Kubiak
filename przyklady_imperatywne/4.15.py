# Napisz program, który realizuje ten sam rodzaj pracy jak w zdaniu 4.8, ale
# z wykorzystaniem funkcji lambda

def main(f=lambda x: x ** 2 + 1):
    krok = 0.5
    x = 0

    print('Program oblicza wartość funckji y = x * x + 1, gdzie x <0, 5> '
          'i rośnie o 0.5:\n')
    while x <= 5:
        y = f(x)
        print(f'x = {x:.2f},\ty = {y:.2f}')
        x += krok


if __name__ == '__main__':
    main()
