import secrets
import string
import time
import os


def print_menu():
    print("|-----------------------------|")
    print("|      PASSWORD GENERATOR     |")
    print("|         PROGRAM MENU        |")
    print("|    1. Generate a password   |")
    print("|    2. Close the program     |")
    print("|-----------------------------|")


def generate_password():
    print("How long should the password be?")
    print()
    range_from = int(input("Minimum length: "))
    range_to = int(input("Maximum length: "))
    print()
    print("Generating password in 5 seconds...")
    time.sleep(5)
    length = secrets.choice(range(range_from, range_to))
    symbols = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(symbols) for i in range(length))
    print(f"Generated password: {password}")


while True:
    print_menu()
    choice = input("Select an option: ")

    if choice == "1":
        generate_password()
    elif choice == "2":
        print("Closing program...")
        time.sleep(1)
        break
    else:
        print("Invalid option.")

    input("Press Enter to continue...")
    os.system('cls')
