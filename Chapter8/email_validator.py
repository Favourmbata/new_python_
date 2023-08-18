import re


def email_validator(list):
    while True:
        email = input("enter your email")
        if len(email) < 8:
            print("email is valid")
        elif not re.search(r'[@][.]',email):
            print("enter invalid email")
        elif not re.search(r'[@][.]',email):
            print(email)

