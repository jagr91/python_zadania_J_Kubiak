# Napisz program, który z pliku Pracownicy.txt odczytuje rekordy i wyświetla je
# na ekranie komputera

def main():
    print('Oczyt z pliku Pracownicy.txt:\n')
    with open("6.5_Pracownicy.txt", 'r', encoding='utf-8') as plik:
        for line in plik.readlines():
            rekord = line.split(';')
            print(f'Imię i nazwisko: {rekord[0]}')
            print(f'Departament: {rekord[1]}')
            print(f'Przełożony: {rekord[2]}')


if __name__ == '__main__':
    main()
