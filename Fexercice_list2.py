liste = ['a', 'b', 'c', 'd']
a = input()


if (a == "r"):
    liste = ['a', 'b', 'c', 'd']
    newliste = liste[-1:] + liste[:-1]
    print(liste)
    print(newliste)
elif (a == "l"):
    liste = ['a', 'b', 'c', 'd']
    newliste = liste[1:] + liste[:1]
    print(liste)
    print(newliste)
else:
    print("error")