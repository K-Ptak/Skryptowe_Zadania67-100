litery = []
liczba = []

with open("danezadanie93.txt", "r") as tekst:
    lines = tekst.readlines()
    for line in lines:
        for x in range(len(line)):
            if line[x].isalnum():
                if not line[x] in litery:
                    litery.append(line[x])
                    liczba.append(1)
                else:
                    liczba[litery.index(line[x])] += 1

for x in range(len(litery)):
    print(f"{litery[x]} : {liczba[x]}")
