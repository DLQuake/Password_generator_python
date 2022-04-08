import secrets
import string as  s
import os
import sys
import time

while True:
    print("|-----------------------------|")
    print("|      PASSWORD GENERATOR     |")
    print("|         PROGRAM MENU        |")
    print("|    1. Generate a password   |")
    print("|    2. Close a program       |")
    print("|-----------------------------|")

    print()
    number = input("Select a number from list: ")
    print()

    if number == "1":
        print("How long the password should be generated?")
        print()
        print("Please enter a range from-to")
        print()
        range_from =int(input("from: "))
        range_to =int(input("to: "))

        print()
        print("The password will be generated in 5 seconds")
        time.sleep(5)
        print()

        length = secrets.choice(range(range_from, range_to))
        symbols = s.ascii_letters + s.digits + s.punctuation
        password = "".join(secrets.choice(symbols) for i in range(length))
        print(f"Generated password by program: {password}")
    elif number == "2":
        sys.exit(0)
    else:
        print("There is no such option")

    number = sys.stdin.read(1)
    os.system('cls')
