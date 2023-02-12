# Napisz program, który oblicza sumę wyrażenia:
# 1 + 3 + 5 + 7 + ... + (2 * n - 1) dla dowolnego n

def oblicz(n):
    s = 0
    for i in range(1, n + 1):
        s = s + 2 * i - 1
    return s


print(oblicz(100))
