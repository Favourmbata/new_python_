num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))

if num1 <= num2 and num1 < num3:
    print(num1, end=" ")
if num2 <= num3:
    print(num2, num3)
else:
    print(num3, num2)

if num2 <= num1 and num3 < num3:
    print(num2, end=" ")
if num1 <= num3:
    print(num1, num3)
else:
    print(num3, num1)

if num3 <= num1 and num3 <= num2:
    print(num3, end=" ")
if num2 <= num1:
    print(num2, num1)
else:
    print(num3, num1)
