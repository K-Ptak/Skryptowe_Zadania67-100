def compareLists(lista1, lista2):
    maxLength = max(len(lista1), len(lista2))

    for index in range(maxLength):
        if index < len(lista1) and index < len(lista2):
            if lista1[index] == lista2[index]:
                print(f"Elementy o indeksie {index} są takie same.  {lista1[index]} == {lista2[index]}")
            else:
                print(f"ROZNICA! {lista1[index]} != {lista2[index]}")
        if index == len(lista1) and index < len(lista2):
            print(f"ROZNICA!: koniec listy 1, {lista2[index]}")
        if index < len(lista1) and index == len(lista2):
            print(f"ROZNICA!: {lista1[index]}, koniec listy 2")


compareLists([1, "abc", True, [1, 2, 3], 'x'], [2, "abc", False, [2, 2, 3], 'x', 'y'])
