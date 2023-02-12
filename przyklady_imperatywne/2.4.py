# Napisz program, który ilustruje działanie operatora or

a = True
b = True

print('Działanie operatora or:')
print(f'a = True, b = True => a or b = {a or b}')
print(f'a = True, b = False => a or b = {a or not b}')
print(f'a = False, b = True => a or b = {not a or b}')
print(f'a = False, b = False => a or b = {not a or not b}')
