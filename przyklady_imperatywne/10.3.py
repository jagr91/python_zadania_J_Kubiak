# Używając funkcji sumowania :
# def sumowanie(N, okres):
#   lączny, k = 0, 1
#   while k <= N:
#       lączny, k = łączny + okres(k), k +1
#   return łączny
# oraz funkcji tożsamościowej, która zwraca swój argument:
#   def identyczność(x):
#       return x
# napisz program, który sumuje liczby naturalne od 1 do N.

def sumowanie(N, okres):
    łączny, k = 0, 1
    while k <= N:
        łączny, k = łączny + okres(k), k + 1
    return łączny


def identyczność(x):
    return x


def sumuj_naturalne(N):
    return sumowanie(N, identyczność)


def main():
    N = 100
    print(sumuj_naturalne(N))


if __name__ == '__main__':
    main()
