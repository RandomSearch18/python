"""R@nd0m P@ssw0rd generator
Have the programme create random strong passwords mixing upper and lower case, symbols and numbers.
Extension:
• Have the password also use ASCII characters
• Have the passwords stored in an external file"""

import secrets


def generate_password(length: int) -> str:
    password = ""
    for _ in range(length):
        # ASCII numbers between 33 and 126 are the alphanumeric and special characters
        range_start = 33
        range_end = 126
        character_code = secrets.randbelow(range_end - range_start) + range_start
        password += chr(character_code)
    return password


if __name__ == "__main__":
    print(generate_password(8))
    print(generate_password(8))
    print(generate_password(8))
    print(generate_password(8))
    print(generate_password(10))
    print(generate_password(12))
    print(generate_password(16))
    print(generate_password(20))
