number = int(input("Enter a number:"))
count = 1
for i in range (1,number + 1):
    count = count * i
print('The factorial of ' , number ,'is' , 'count',count)