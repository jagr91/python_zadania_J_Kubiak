# Napisz program, który wyświetla duże litery alfabetu od A do Z i od Z do A z
# wykorzystaniem pętli for

for i in range(65, 91):
    print(chr(i), end=' ')

print()

for i in range(90, 64, -1):
    print(chr(i), end=' ')
