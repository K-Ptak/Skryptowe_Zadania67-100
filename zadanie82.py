lista = []

with open('zadanie82.txt') as plik:
    lines = plik.read().splitlines()
    for line in lines:
        lista.append(int(line))

print(sum(lista))
print(sum(lista)/len(lista))

if(len(lista)%2==0):
    print(((lista[int(len(lista)/2)]-1)+(lista[int(len(lista)/2)]+1))/2)
else:
    print(lista[int(len(lista)/2)])
