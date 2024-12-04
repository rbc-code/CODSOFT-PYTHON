import random
import string
def generate_password():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be greater than zero.")
            return
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation
        all_characters = lowercase + uppercase + digits + symbols
        password = ''.join(random.choice(all_characters) for _ in range(length))
        print(f"Your generated password is: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")
if __name__ == "__main__":
    generate_password()
