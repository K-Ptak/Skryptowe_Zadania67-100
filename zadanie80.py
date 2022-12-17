liczba = input("Wprowadz liczbe: ")

try:
    value = int(liczba)
except ValueError:
    print("Wprowadzono zla wartosc")
