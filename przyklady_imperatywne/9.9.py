# Napisz program, który z wykorzystaniem nieskończonego generatora,
# znjaduje kolejne wyrazy ciągu Fibbonaciego.

def ciag_fib():
    k0, k1 = 0, 1
    yield k0
    yield k1
    while True:
        k0, k1 = k1, k0 + k1
        yield k1


a = ciag_fib()
for i in range(15):
    print(next(a))
