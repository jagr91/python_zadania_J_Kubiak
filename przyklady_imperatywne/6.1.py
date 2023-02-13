# Napisz program, który zapisuje dane: imię i nazwisko w pliku tekstowym
# test.txt a następnie odczytuje dane z pliku tekstowego i wyświetla na
# ekranie komputera

dane = input('Podaj imię i nazwisko: ')

with open('6.1_test.txt', 'w', encoding='utf-8') as file:
    file.write(dane)

with open('6.1_test.txt', 'r', encoding='utf-8') as file:
    print(file.read())
