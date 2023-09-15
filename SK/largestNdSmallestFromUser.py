largest = 0
smallest = 0
while True:
    try:
        number = int(input("Enter a number (or -1 to break):"))
        if number == -1:
            break
        if number > largest:
          largest = number
        else:
          smallest = number
    except ValueError:
        print("Enter a valid number")

print("The largest is ->" ,largest)
print("The smallest is -> ",smallest)