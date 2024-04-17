# Extraire le mot python
chaine = "Python est un langage de programmation puissant et facile à apprendre."
# Recherche de l'indice du mot "Python"
indice_python = chaine.find("Python")
# Extraction du mot "Python" en utilisant l'indice
mot_python = chaine[indice_python:indice_python + len("Python")]
print(mot_python)  # Output: Python
# Extraire apprendre en utlisant les indices
mot_apprendre = chaine.split()[-1]
print(mot_apprendre)  # Output: apprendre
phrase = chaine[chaine.find("langage"):chaine.find("puissant") + len("puissant")]
print(phrase)  # Output: langage de programmation
# Inverser la chaine de caractère
chaine_inverse = chaine[::-1]  # commencer a partir de la fin
print(chaine_inverse)
# Output: ".erdnerppa à elicaf te tnatsiup ed tniamuorp ed egagneal nu tse nohtyP"

