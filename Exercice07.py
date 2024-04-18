def decode_message(encoded_message):
    # Split the encoded message into individual numbers
    numbers = encoded_message.split()

    # Convert each number to its corresponding ASCII character and join them to form the decoded message
    decoded_message = ''.join(chr(int(num)) for num in numbers)

    return decoded_message

# Example encoded message
encoded_message = "65 77 73 84 32 75 85 77 65 82 32 68 69 89"

# Decode the message
decoded_message = decode_message(encoded_message)

# Print the decoded message
print("Decoded Message:", decoded_message)
