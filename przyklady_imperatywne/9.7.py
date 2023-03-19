# Napisz program, który za pomocą generatora, teorzy ciąg liczb od 10 do 0

def generator(number):
    while number > -1:
        yield number
        number -= 1


def main():

    gen = generator(10)

    for i in range(11):
        print(gen.__next__())


if __name__ == '__main__':
    main()
