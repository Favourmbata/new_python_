number = int(input("enter a number:"))
count = 1
if number >= 1:
   for num in range(1,number +1):
       count = count * num
print("The factorial of number is:",count)