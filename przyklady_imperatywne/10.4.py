# # Używając funkcji sumowania :
# def sumowanie(N, okres):
#   lączny, k = 0, 1
#   while k <= N:
#       lączny, k = łączny + okres(k), k +1
#   return łączny
# oraz funkcji:
#   def pi_term(i):
#       return 8 / ((4 * i - 3) * (4 * i -1))
# któa wylicza i-ty wyraz ciągu, oblicz przybliżoną wartość liczby pi.
import math


def sumowanie(N, okres):
    łączny, k = 0, 1
    while k <= N:
        łączny, k = łączny + okres(k), k + 1
    return łączny


def pi_term(i):
    return 8 / ((4 * i - 3) * (4 * i - 1))


def pi_n(N):
    return sumowanie(N, pi_term)


def main():
    N = 1e6
    print('Oblicznaie pi. Proszę czekać...')
    print(f'Wartośc obliczonego pi to: {pi_n(N)}')
    print(f'Wartość pi z modułu math: {math.pi}')


if __name__ == '__main__':
    main()
