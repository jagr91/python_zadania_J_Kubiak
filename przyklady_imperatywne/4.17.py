# Napisz program, który iteracyjnie znajduje wszystkie czwórki pitagorejskie z
# przdziału od 1 do N.
# W zadaniu N = 10

def czworki_pit(N):
    for a in range(1, N):
        for b in range(1, N):
            for c in range(1, N):
                for d in range(1, N):
                    if a * a + b * b + c * c == d * d:
                        print(f'{a}, {b}, {c}, {d}')


def main():
    print('Program znajduję czwórki pitagorejskie z zakresu <1:10>\n')
    czworki_pit(10)


if __name__ == '__main__':
    main()
