# Napisz program, który zapisuje dane: imię i nazwisko w pliku tekstowym
# test.txt a następnie odczytuje dane z pliku tekstowego i wyświetla na
# ekranie komputera

dane = input('Podaj imię i nazwisko: ')
path = (r'D:\G\OneDrive\G\Nauka\Python\Books\python - zadania z programowania'
        r'\przyklady_imperatywne\6.1_test.txt')

with open(path, 'w') as file:
    file.write(dane)

with open(path, 'r') as file:
    print(file.read())
