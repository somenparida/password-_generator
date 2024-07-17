import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_punctuation=True):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not any([use_lowercase, use_uppercase, use_digits, use_punctuation]):
        return "Error: At least one character set must be selected."

    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("Password Generator")

while True:
    try:
        length = int(input("Enter the desired length of the password (or enter 0 to quit): "))
        if length == 0:
            print("Exiting password generator.")
            break

        use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_punctuation = input("Include punctuation? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_punctuation)
        print("Generated Password:", password)
    
    except ValueError:
        print("Invalid input! Please enter a valid number for password length.")
    except Exception as e:
        print("An error occurred:", e)
