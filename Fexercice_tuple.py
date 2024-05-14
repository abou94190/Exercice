def tuple_max_elements(tuple_list):
    if not tuple_list:
        return None  # Si la liste est vide, retourne None

    max_length = -1
    max_tuple = None

    for tup in tuple_list:
        current_length = len(tup)
        if current_length > max_length:
            max_length = current_length
            max_tuple = tup

    return max_tuple

# Exemple d'utilisation


tuple_list = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10)]
resultat = tuple_max_elements(tuple_list)

if resultat:
    print("Le tuple avec le plus d'éléments est :", resultat)
else:
    print("La liste est vide.")
