characters = ['A', 'b', 'C', 'd', 'E', 'F', 'g', 'H', 'I']

# Extract capital letters
capital_letters = [1 for char in characters if char.isupper()]
C=sum(capital_letters)

# Extract smaller letters
smaller_letters = [1 for char in characters if char.islower()]
S=sum(smaller_letters)

print("Total Capital letters:", C)
print("Total Smaller letters:", S)


