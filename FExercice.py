characters = ['A', 'b', 'C', 'd', 'E', 'F', 'g', 'H', 'I']

# Extract capital letters
capital_letters = [char for char in characters if char.isupper()]

# Extract smaller letters
smaller_letters = [char for char in characters if char.islower()]

print("Capital letters:", capital_letters)
print("Smaller letters:", smaller_letters)
