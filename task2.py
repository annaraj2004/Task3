import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password_list = [random.choice(characters) for _ in range(length)]
    password = ''.join(password_list)
    return password

def password_generator():
    try:
        length = int(input("Enter the length of the password: "))

        if length <= 0:
            print("Password length must be greater than 0.")
            return

        password = generate_password(length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    password_generator()