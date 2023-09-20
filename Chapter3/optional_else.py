for i in range(2):
    value = int(input("Enter an intger (-1 to break): "))
    print("you entered value:", value)
    if value == -1:
        break
else:
    print("The loop will terminate without executing the break")
