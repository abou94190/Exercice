def trouver_intersection(set1, set2):
    intersection = set1.intersection(set2)
    return intersection


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

resultat_fonction = trouver_intersection(set1, set2)

print(resultat_fonction)