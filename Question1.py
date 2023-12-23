# This program used to encrypt or decrypt a message using the Caesar cipher
def caesar_cipher(message, key, mode):
    # Initialize an empty string to store the encrypted or decrypted message
    encrypted_message = ""
    # Loop through each character in the message
    for char in message:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Ensure the shift remains within 0-25
            shift = key % 26

            # Encrypting lowercase letters
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            # Encrypting uppercase letters
            elif char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # Add the encrypted character to the result
            encrypted_message += encrypted_char
        else:
            # For non-alphabet characters, just append as-is
            encrypted_message += char

    return encrypted_message

# Display the program logic
print("Do you want to (e)ncrypt or (d)ecrypt?")
choice = input("> ").lower()

if choice in ['e', 'd']:
    key_input = input("Please enter the key (0 to 25) to use.\n> ")

    if key_input.isdigit() and 0 <= int(key_input) <= 25:
        key = int(key_input)
    else:
        print("Invalid key value. Exiting.")
        exit()

    message = input("Enter the message to {}.\n> ".format("encrypt" if choice == 'e' else "decrypt"))
    result = caesar_cipher(message, key if choice == 'e' else -key, choice)
    print(result)
    # Display a note to inform the user
    print("Full encrypted/decrypted text copied to clipboard.")
else:
    print("Invalid choice. Exiting.")
    exit()
