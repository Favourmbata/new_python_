import re


def validate_password():
    while True:
        password = input("Enter passord")
        if len(password)< 8:
            print("password must be 8 character long")
        elif not re.search(r'[A-Z]' ,password):
            print("password must contain one upperCase")
        elif not  re.search(r'[a-z]',password):
         print("password must contain one lowerCase")
        elif not re.search(r'[0-9]',password):
          print("password must  contain one number")
        else:
            print("password is invalid")
            return password

valid_password = validate_password()
print("valid password:"+valid_password)







