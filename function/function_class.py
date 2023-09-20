def get_price(number_of_copies):
    if 1 <= number_of_copies <= 4:
        return 2000
    elif number_of_copies <= 9:
        return 1800
    elif number_of_copies <= 29:
        return 1600
    elif number_of_copies <= 49:
        return 1500
    elif number_of_copies <= 99:
        return 1300
    elif number_of_copies <= 199:
        return 1200
    elif number_of_copies <= 499:
        return 1100

    return 1000
