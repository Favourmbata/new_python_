# age = int(input("Enter an age"))
#
# result = "not Eligible" if age < 18 else "Eligible"
# print(result)


language = input("Enter your language:")

match language:
    case "yoruba":
        print("welcome to ibandan:")
    case "Igbo":
        print("welcome to anambra")
    case "Hausa":
        print("welcome to kano")
    case _:
        print("You're not from here")
