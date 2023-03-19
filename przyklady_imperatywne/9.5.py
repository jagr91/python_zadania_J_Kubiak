# Napisz program, który wykorzystuje działąnie iteratora range().

def main():
    Lista = list(range(1, 10))
    print(f'Lista = {Lista}.', sep="")
    print()

    for i in Lista:
        print(i)


main()
