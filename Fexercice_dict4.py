def pal(mot):
    mot = mot.lower()
    return mot == mot[::-1]


list = ['hello', 'level', 'pop', 'green']
npal = 0
for mot in list:
    if pal(mot):
        npal += 1
print(npal)