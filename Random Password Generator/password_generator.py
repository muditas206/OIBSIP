import random
import string

def generate_password():
    print("=== Random Password Generator ===\n")

    # Length input
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))
            if length < 8:
                print("Length must be at least 8. Please try again.\n")
                continue
            break
        except ValueError:
            print("Please enter a valid number.\n")

    # Character types
    print("\nSelect character types (at least 2 required):")
    use_upper = input("Include Uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include Lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include Numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include Symbols? (y/n): ").lower() == 'y'

    # Count selected types
    selected = sum([use_upper, use_lower, use_digits, use_symbols])
    if selected < 2:
        print("\nError: Please select at least 2 character types.")
        return

    # Build character pool
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    print("\n" + "="*40)
    print(f"Generated Password: {password}")
    print("="*40)

    # Generate again option
    again = input("\nGenerate another password? (y/n): ").lower()
    if again == 'y':
        print()
        generate_password()


if __name__ == "__main__":
    generate_password()