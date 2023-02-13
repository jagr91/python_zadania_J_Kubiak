# Napisz program, w którym zawarto opcję usuwania wybranego rekordu z pliku
# Pracownicy.txt

dane = input('Podaj imię i nazwisko do usunięcia: ')


def main():
    with open("6.5_Pracownicy.txt", 'r', encoding='utf-8') as plik:
        filedata = plik.readlines()
        splitlist = [i.split(';')for i in filedata]
        for item in splitlist:
            item[2] = item[2].strip('\n')
            # usuń znak nowego wiersza na końcu ('\n')
        for item in splitlist:
            if dane != item[0]:
                print(f'Nie znaleziono pracownika {dane}')
                break
            else:
                print(f'Znaleziono i usunięto pracownika {item[0]}')
                splitlist.remove(item)
                break
    with open("6.5_Pracownicy.txt", 'w', encoding='utf-8') as plik:
        for item in splitlist:
            if splitlist.index(item) + 1 != len(splitlist):
                # nie dodawaj nowej linii w ostatnim rekordzie
                plik.writelines([item[0], ';', item[1], ';', item[2], '\n'])
            else:
                plik.writelines([item[0], ';', item[1], ';', item[2]])


if __name__ == '__main__':
    main()
