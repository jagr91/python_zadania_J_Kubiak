# Napisz program, który modyfikuje wybrany rekord z pliku Pracownicy.txt.
# Do modyfikowania rekordu wykorzystaj pole dane zawierające
# imię i nazwisko pracownika

dane = input('Podaj imię i nazwisko do edycji: ')


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
                print(f'Znaleziono pracownika {item[0]}')
                item[0] = input("Podaj nowe imię i nazwisko: ")
                item[1] = input("Podaj nowy departament: ")
                item[2] = input("Podaj nowego przełożonego: ")
                print(f'\nZmieniono dane pracownika {item[0]}')
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
