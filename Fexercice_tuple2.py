def reverse_tuples(listes_tuples):
    # Crée une nouvelle liste pour stocker les tuples inversés
    reversed_list = []

    # Parcourt chaque tuple dans la liste de tuples donnée
    for tup in listes_tuples:
        # Inverse l'ordre des éléments dans le tuple en utilisant tup[::-1]
        reversed_tuple = tup[::-1]
        # Ajoute le tuple inversé à la nouvelle liste
        reversed_list.append(reversed_tuple)

    return reversed_list

# Exemple d'utilisation avec la même liste de tuples


liste_tuples = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10)]
resultat_inverse = reverse_tuples(liste_tuples)

# Affiche les tuples inversés
print("Liste de tuples initiale :", liste_tuples)
print("Liste de tuples avec l'ordre inversé des éléments :", resultat_inverse)
