
first_name = str(input(" enter your first_name:"))
if first_name is None or first_name == "":
    print("your name cannot be empty:")
    exit()
last_name = str(input('enter your last_name:'))
if last_name is None or last_name =="":
    print("your name cannot be an empty string:")
    exit()
age = int(input("enter your age"))
if age < 18:
    print("you are underage")
if age > 65:
    print("you are an old citizen")
