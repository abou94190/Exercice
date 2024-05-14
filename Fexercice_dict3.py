def trouver_plus_grand(a, b, c):
    # Compare les trois nombres pour trouver le plus grand
    plus_grand = a  # Supposons initialement que 'a' est le plus grand
    
    if b > plus_grand:
        plus_grand = b  # Met à jour si 'b' est plus grand que précédent
    
    if c > plus_grand:
        plus_grand = c  # Met à jour si 'c' est plus grand que précédent
    
    return plus_grand

# Lecture des trois nombres en entrée


a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))
c = float(input("Entrez le troisième nombre : "))

# Appel de la fonction pour trouver le plus grand nombre parmi les trois
resultat = trouver_plus_grand(a, b, c)

# Affichage du résultat
print("Le plus grand nombre parmi", a, ",", b, "et", c, "est :", resultat)
