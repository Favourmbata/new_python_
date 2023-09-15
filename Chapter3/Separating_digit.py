user_input = int(input("Enter five digit "))

if user_input <= 10000 or user_input <= 99999:
    digit1 =  user_input // 10000
    digit2 = user_input // 1000 % 10
    digit3 = user_input // 100 % 10
    digit4 = user_input  // 10 % 10
    digit5 = user_input % 10

    print(f"{digit1}  {digit2}  {digit3}   {digit4}   {digit5}")
else:
    print("Enter a valid number")