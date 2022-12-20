import random

try:
    with open("danezadanie85.txt", "r") as plik:
        fileList = plik.read().splitlines()

except IOError:
    print("Blad otwierania pliku")
    exit()

a = random.randint(1, 100)
b = random.choice(fileList)

try:
    outputFile = open("wynikzadanie85.txt", "w")

except IOError:
    print("Blad otwierania pliku")
    exit()

outputFile.write(str(a)+"\n")
outputFile.write(str(b))
outputFile.close()