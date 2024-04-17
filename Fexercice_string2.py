# Extraire le mot python
chaine = "Python est un langage de programmation puissant et facile à apprendre."
mot_python = chaine.split()[0]
print(mot_python)  # Output: Python
# Extraire apprendre en utlisant les indices
mot_apprendre = chaine.split()[-1]
print(mot_apprendre)  # Output: apprendre
phrase = chaine[chaine.find("langage"):chaine.find("puissant") + len("puissant")]
print(phrase)  # Output: langage de programmation
# Inverser la chaine de caractère
chaine_inverse = chaine[::-1]
print(chaine_inverse)
# Output: ".erdnerppa à elicaf te tnatsiup ed tniamuorp ed egagneal nu tse nohtyP"

