# create a Function to perform Caesar cipher encryption or decryption
def caesar_cipher(text, key, mode):
    # Initialize an empty string to store the result
    result = ""
    # Ensure the key is within the range of 0-25
    key %= 26

    for char in text:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Encrypt lowercase letters
            if char.islower():
                result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            # Encrypt uppercase letters
            elif char.isupper():
                result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            # For non-alphabetic characters, append as-is
            result += char
    return result


# Get user's choice: encrypt or decrypt
while True:
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    choice = input("> ").lower()

    if choice in ['e', 'd']:
        # Exit the loop if valid choice is provided
        break
    else:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")

# Get the key from the user
while True:
    key = int(input("Please enter the key (0 to 25) to use.\n> "))

    if 0 <= key <= 25:
        # Exit the loop if valid key is provided
        break
    else:
        print("Invalid key value. Please enter a number between 0 and 25.")

# Get the message to encrypt or decrypt
message = input(f"Enter the message to {'encrypt' if choice == 'e' else 'decrypt'}.\n> ")

# Perform encryption or decryption based on user's choice
result = caesar_cipher(message, key if choice == 'e' else -key, choice)

# Display the result
print(result)
print("Note: The encrypted/decrypted text is displayed above.")
