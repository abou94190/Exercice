a = [1, 2, 3]
#  la commande qui permet de transformer en ASCCI
b = bytearray(a)
#  Changer le premier element en "a"
b[0] = 97
#  Afficher le code ASCCI
print(b)