# Korzystając z operatorów and, or i not, napisz program, który sprawdza
# pierwsze prawo De Morgana.
# I Prawo De Morgana: Zaprzeczenie koniunkcji dwóch zdań  jest równoważne
# alternatywie zaprzeczeń tych zdań => not (a and b) =  not a or not b

a = True
b = False

lewa_strona = not a and not b
prawa_strona = not a or not b

if lewa_strona == prawa_strona:
    print(f'a = {a}, b = {b} => {lewa_strona} == {prawa_strona}')
    print('Równanie spełnia Prawo De Morgana')
else:
    print(f'a = {a}, b = {b} => {lewa_strona} =/= {prawa_strona}')
    print('Równanie nie spełnia Prawa De Morgana')
