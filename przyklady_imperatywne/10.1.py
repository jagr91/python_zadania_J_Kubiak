# Napisz program, w którym wykorzystano funkcje wyższego rzędu

def f_x_pct(f):
    def f2(przychod):
        return f(f(przychod))
    return f2


podatek = lambda x: x * 0.18

oblicz_podatek = f_x_pct(podatek)

print(oblicz_podatek(10000))
