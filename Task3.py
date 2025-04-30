import secrets
import string
import pyperclip

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    """
    Generate a secure random password based on user-specified character sets.

    Args:
        length (int): Desired length of the password.
        use_uppercase (bool): Whether to include uppercase letters.
        use_lowercase (bool): Whether to include lowercase letters.
        use_digits (bool): Whether to include digits.
        use_symbols (bool): Whether to include symbols.

    Returns:
        str: The generated password.
    """
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected!")

    # Generate password using secrets.choice for strong randomness
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def copy_to_clipboard(password):
    """
    Copy the given password to the system clipboard.

    Args:
        password (str): The password to be copied.
    """
    pyperclip.copy(password)
    print("Password has been copied to clipboard!")

def get_user_input():
    """
    Prompt the user to enter password generation preferences.

    Returns:
        tuple: (length, use_uppercase, use_lowercase, use_digits, use_symbols, number_of_passwords)
    """
    try:
        length = int(input("Enter password length: "))
        number_of_passwords = int(input("How many passwords to generate? "))
        
        print("\nInclude the following in password:")
        use_uppercase = input("Include Uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include Lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include Digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include Symbols? (y/n): ").lower() == 'y'

        if length <= 0 or number_of_passwords <= 0:
            raise ValueError

        return length, use_uppercase, use_lowercase, use_digits, use_symbols, number_of_passwords

    except ValueError:
        print("Invalid input! Please enter positive numbers and valid choices.")
        return get_user_input()  # Retry input on error

def main():
    """
    Main function to drive the password generator tool.
    """
    print("🔐 Welcome to Secure Password Generator 🔐")
    length, use_uppercase, use_lowercase, use_digits, use_symbols, number_of_passwords = get_user_input()

    passwords = []

    for _ in range(number_of_passwords):
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        passwords.append(password)

    print("\nGenerated Password(s):")
    for idx, pwd in enumerate(passwords, 1):
        print(f"{idx}. {pwd}")

    # Offer option to copy the last generated password
    copy_choice = input("\nDo you want to copy the last password to clipboard? (y/n): ").lower()
    if copy_choice == 'y':
        copy_to_clipboard(passwords[-1])

if __name__ == "__main__":
    main()
