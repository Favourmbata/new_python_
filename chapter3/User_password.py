user_name = 10
user = input("choose a user name:[4_10] characters")
if 4 <= len(user_name)<=10:
    print(f"Thank you{user_name}is valid")
else:
    print("The user name must be between 4 and 10 characters long")