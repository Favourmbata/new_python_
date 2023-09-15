user_input = int(input("Enter five digit"))
if 10000 <= user_input <= 99999:

    digit_1 = user_input // 10000
    digit_2 = user_input // 1000 % 10
    digit_3 = user_input // 100 % 10
    digit_4 = user_input // 10 % 10
    digit_5 = user_input % 10

    print(f"{digit_1}  {digit_2}  {digit_3}  {digit_4} {digit_5}")
else:
    print("Enter a valid five digit")

