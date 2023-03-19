# Napisz program, w którym znajduje się najprostszy przykład generatora
# zwracającego kollejne liczby nieparzyste od 1 do 100

def generator(num):
    for i in range(1, num+1):
        if i % 2 == 1:
            yield i


def main():
    gen = generator(100)
    print('Lista liczb nieparzystych od 1 do 100:')
    print(list(gen))


if __name__ == '__main__':
    main()
