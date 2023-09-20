number = int(input("Enter an integer"))
sum_element = 0
product = 1
smallest = 0
largest = 0
for i in range(4):
    sum_element = sum_element + number
    product *= number
    if largest > number:
        largest = number
    if smallest < number:
        smallest = number
print("the sum of number:", sum_element)
average = sum_element / 4
print("Average is of number:", average)
print("The product of numbers:", product)
print("The largest number is", largest)
print("The smallest is",smallest)