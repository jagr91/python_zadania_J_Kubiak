# Napisz powyzszy program (10.1), w którym zastosowano składnie dekoratora

def f_x_pct(f):
    def f2(przychod):
        return f(f(przychod))
    return f2


def main():
    @f_x_pct
    def g(x):
        return x * 0.18
    print(g(10000))


if __name__ == '__main__':
    main()
