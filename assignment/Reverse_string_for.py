def reverse_String(rev):
    rev1 = " "
    for i in rev:
        rev1 = i + rev1
        return rev1
rev = "javapoint"
print("The original string is: ",rev)

print("The reverse string is ",reverse_String(rev))