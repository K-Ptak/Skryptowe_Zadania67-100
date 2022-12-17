def czyNalezy(lista1, lista2, szukane):
    for element in lista1:
        if element == szukane:
            print("Znaleziono element w liscie1")
    for element in lista2:
        if element == szukane:
            print("Znaleziono element w liscie2")


czyNalezy([1, "abc", True, [1, 2, 3], 'x'], [2, "abc", False, [2, 2, 3], 'x', 'y'], 'y')
