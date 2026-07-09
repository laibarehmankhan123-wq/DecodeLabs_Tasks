import string
import random
import math

def get_password_length():
    while True:
        raw_input_value = input("Enter desired password length (e.g., 16): ").strip()

        if not raw_input_value.isdigit():
            print("Invalid input. Please enter a whole number (e.g., 16).\n")
            continue

        length = int(raw_input_value)

        if length <= 0:
            print("Password length must be a positive integer.\n")
            continue

        if length > 64:
            print("Length capped at 64 characters. Try a smaller value.\n")
            continue

        if length < 15:
            print("Warning: NIST 2024 guidelines recommend a minimum of "
                  "15 characters for high-security contexts.")

        return length


def get_character_preferences():
    include_symbols = input(
        "Include special symbols (@, #, $, etc.)? (y/n): "
    ).strip().lower().startswith("y")

    return include_symbols

def generate_password(length, include_symbols=False):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    character_pool = letters + digits
    if include_symbols:
        character_pool += symbols

    required_chars = [
        random.choice(string.ascii_letters),
        random.choice(string.digits),
    ]
    if include_symbols:
        required_chars.append(random.choice(symbols))

    remaining_length = length - len(required_chars)
    random_chars = [random.choice(character_pool) for _ in range(remaining_length)]

    all_chars = required_chars + random_chars
    password_list = []
    while all_chars:
        index = random.choice(range(len(all_chars)))
        password_list.append(all_chars.pop(index))
    password = ''.join(password_list)
    return password, len(character_pool)

def calculate_entropy(length, pool_size):
    return length * math.log2(pool_size)


def describe_strength(entropy_bits):
    if entropy_bits < 40:
        return "Weak"
    elif entropy_bits < 60:
        return "Moderate"
    elif entropy_bits < 80:
        return "Strong"
    else:
        return "Very Strong"


def main():
    print("=" * 55)
    print("Random Password Generator")
    print("=" * 55)

    length = get_password_length()
    include_symbols = get_character_preferences()

    password, pool_size = generate_password(length, include_symbols)
    entropy_bits = calculate_entropy(length, pool_size)
    strength = describe_strength(entropy_bits)

    print("\n--- Generated Password ---")
    print(password)
    print(f"\nLength: {length} characters")
    print(f"Character pool size: {pool_size}")
    print(f"Entropy: {entropy_bits:.2f} bits")
    print(f"Strength rating: {strength}")
    print("=" * 55)


if __name__ == "__main__":
    main()