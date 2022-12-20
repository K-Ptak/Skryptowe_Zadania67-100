with open("danezadanie91.txt", "r") as plik:
    try:
        input = int(plik.readline())
    except ValueError:
        print("W pliku nie znaleziono liczby")

with open("wyjsciezadanie91.txt", "w") as output:
    try:
        output.write(f"{bin(input)[2:]} \n")
        output.write(f"{oct(input)[2:]} \n")
        output.write(f"{hex(input)[2:]} \n")
    except FileNotFoundError:
        print("Nie znaleziono pliku")