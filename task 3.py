# password_generator.py

import string
import random

def generate_password(length: int, use_upper: bool = True, use_digits: bool = True, use_symbols: bool = True) -> str:
    if length < 4:
        raise ValueError("Password length should be at least 4 characters for good security.")

    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase if use_upper else ''
    digit_chars = string.digits if use_digits else ''
    symbol_chars = string.punctuation if use_symbols else ''

    all_chars = lower_chars + upper_chars + digit_chars + symbol_chars

    if not all_chars:
        raise ValueError("At least one character set must be selected.")
    password = [
        random.choice(lower_chars),
        random.choice(upper_chars) if use_upper else '',
        random.choice(digit_chars) if use_digits else '',
        random.choice(symbol_chars) if use_symbols else ''
    ]

    password += random.choices(all_chars, k=length - len(password))
    random.shuffle(password)

    return ''.join(password)

def main() -> None:
    print("=== Password Generator ===")
    try:
        length = int(input("Enter the desired password length: "))
        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (e.g. @#$%) (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_upper, use_digits, use_symbols)
        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
