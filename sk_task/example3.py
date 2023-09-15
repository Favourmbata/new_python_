num1 = int(input("Enter first number->"))
num2 = int(input("Enter second number->"))
num3 = int(input("Enter third number->"))
#
# largest_number = max(num1,num2,num3)
# smallest_number = min( num1,num2,num3)
#
# print("The largest_number is" ,largest_number)
# print("The smallest_number is ", smallest_number)


if num1 > num2 and num1 > num3:
    print("The highest_number is ", num1)

elif num2 > num1 and num2 > num3:
    print("is the highest number->",num2)
else:
    print("is the highest number is->",num3)


if num1 < num2 and num1 < num3:
    print("The smallest number is->",num1)
elif num2 < num1 and num2 < num3:
    print("The smallest is ->",num2)
else:
    print("The smallest is number ->",num3)