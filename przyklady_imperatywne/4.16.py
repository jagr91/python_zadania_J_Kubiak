# Napisz program, który iteracyjnie znajduje wszystkie trójki pitagorejskie z
# przdziału od 1 do N.
# W zadaniu N = 10

def czworki_pit(N):
    for a in range(1, N):
        for b in range(1, N):
            for c in range(1, N):
                if a * a + b * b == c * c:
                    print(f'{a}, {b}, {c}')


def main():
    print('Program znajduję trójki pitagorejskie do zakresu <1:30>\n')
    czworki_pit(30)


if __name__ == '__main__':
    main()
