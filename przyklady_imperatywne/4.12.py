# Napisz program, który wyświetla 10 początkowych liczb ciągu Fibbonaciego i
# wyświetla je na ekranie komputera

# n = 0 >> fib(n) = 0
# n = 1 >> fib(n) = 1
# n >=2 >> fib(n) = fib(n-1) + fib(n-2)

def fib(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fib(a - 1) + fib(a - 2)


def main():
    print('Program wyświetla 10 pierwszych liczb ciągu Fibbonaciego:\n')
    for i in range(11):
        print(f'f({i}) = {fib(i)}')


if __name__ == '__main__':
    main()
