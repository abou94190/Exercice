def trouver_difference_symetrique(ensemble1, ensemble2):
    # la méthode symmetric_difference pour trouver la différence symétrique
    difference_symetrique = ensemble1.symmetric_difference(ensemble2)
    return difference_symetrique

# Exemple d'utilisation


ensemble1 = {1, 2, 3, 4, 5}
ensemble2 = {4, 5, 6, 7, 8}

# Appel de la fonction pour trouver la différence symétrique des deux ensembles
resultat_diff_symetrique = trouver_difference_symetrique(ensemble1, ensemble2)

# Affichage du résultat
print("Ensemble 1 :", ensemble1)
print("Ensemble 2 :", ensemble2)
print("Différence symétrique des ensembles :", resultat_diff_symetrique)
