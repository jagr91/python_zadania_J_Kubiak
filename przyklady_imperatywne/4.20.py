# Napisz program, który oblicza sumę wyrażenia:
# 1 * 2 + 2 * 3 + 3 * 4 + ... + 4 + n * (n + 1) dla dowolnego n

def oblicz(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i * (i + 1)
    return s


print(oblicz(100))
