

def contains_digit(password):
    digitCounter = 0
    for eachLetter in password:
        if eachLetter.isdigit():
            digitCounter = digitCounter + 1
    return digitCounter;


def has_upper(password):
    digitCounter = 0
    for eachLetter in password:
        if eachLetter.isupper():
            digitCounter = digitCounter + 1
    return digitCounter;


def has_lower(password):
    digitCounter = 0
    for eachLetter in password:
        if eachLetter.islower():
            digitCounter = digitCounter + 1
    return digitCounter;


def eight_characters(password):
    if len(password) <= 8:
        return True


def password_validator(password):
    password = input("Enter password -> ")
    error_counter = 0
    if not (contains_digit(password)):
        error_counter = error_counter + 1
        print("Password must contain digit")
    if not (has_upper(password)):
        error_counter = error_counter + 1
        print("Password must contain an uppercase")
    if not (has_lower(password)):
        error_counter = error_counter + 1
        print("Password must contain a lowercase")
    if not (eight_characters(password)):
        error_counter = error_counter + 1
        print("Password must contain 8 character")
    if error_counter == 0:
        print(password)
    else:
        password_validator(password)


password_validator("password")
