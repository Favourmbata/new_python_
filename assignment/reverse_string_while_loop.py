reverse = "Javapoint"
print("The original string is:",reverse)

reverse_String = " "
count = len(reverse)
while count > 0:
    reverse_String += reverse[count -1]
    count = count -1
print("The reverse string using a while loop is :",reverse_String)