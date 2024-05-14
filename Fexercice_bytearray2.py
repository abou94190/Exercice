liste = [2, 4, 6, 8]
ba = bytearray(liste)
print(ba)
for index, element in enumerate(ba):
    print("Élément à l'index", index, ":", element)
    ba[index] = element + 1
print(list(ba))
