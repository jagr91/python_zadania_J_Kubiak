# Następujący fraagment kodu programu:
#     a = b
#     b = 5
#
#     operacja = 'dodawanie'
#
#     if operacja == 'dodawanie':
#         wynik = a + b
#     else:
#         wynik = a - b
#
#     print(wynik)
# napisz na nowo z wykorzystaniem trójargumentowej instrukcji warunkowej

a = 5
b = 5
operacja = 'dodawanie'

wynik = a + b if operacja == 'dodawanie' else a - b
print(f'Wynik = {wynik}')
