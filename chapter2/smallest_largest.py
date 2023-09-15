num1 =int(input("Enter first number1->"))
num2 = int(input("Enter second number2->"))
num3 = int(input("Enter third number3->"))


sum = num1 + num2 + num3
product = num1 * num2 * num3

average = (num1 + num2 + num3)/3
largest_number = max(num1,num2,num3)
smallest_number = min(num1,num2,num3)
print( 'The sum is',sum)
print('The product is', product)
print('The average is', average)
print('The largest_number is',largest_number)
print('The smallest_number is',smallest_number)

#
#
# def main():
#
#     numbers = [int(input("Enter number {}:".format(i + 1))) for i in range(3)]
#
#     sum_result = reduce(lambda x, y: x + y, numbers)
#
#     average = sum_result / len(numbers)
#
#     product = reduce(lambda x, y: x * y, numbers)
#
#     smallest = reduce(lambda x, y: x if x < y else y, numbers)
#     largest = reduce(lambda x, y: x if x > y else y, numbers)
#
#     print("Sum:", sum_result)
#     print("Average:", average)
#     print("Product:", product)
#     print("Smallest:", smallest)
#     print("Largest:", largest)
#
# if __name__ == "__main__":
#     from functools import reduce
#     main()



# def sum_numbers(numbers):
#   sum = 0
#   for number in numbers:
#     sum += number
#   return sum
#
# def average_numbers(numbers):
#   sum = sum_numbers(numbers)
#   return sum / len(numbers)
#
# def product_numbers(numbers):
#   product = 1
#   for number in numbers:
#     product *= number
#   return product
#
# def smallest_number(numbers):
#   smallest_number = numbers[0]
#   for number in numbers:
#     if number < smallest_number:
#       smallest_number = number
#   return smallest_number
#
# def largest_number(numbers):
#   largest_number = numbers[0]
#   for number in numbers:
#     if number > largest_number:
#       largest_number = number
#   return largest_number
#
# def main():
#   numbers = []
#   for i in range(3):
#     number = int(input("Enter number {}: ".format(i + 1)))
#     numbers.append(number)
#
#   print("The sum of the numbers is {}".format(sum_numbers(numbers)))
#   print("The average of the numbers is {}".format(average_numbers(numbers)))
#   print("The product of the numbers is {}".format(product_numbers(numbers)))
#   print("The smallest number is {}".format(smallest_number(numbers)))
#   print("The largest number is {}".format(largest_number(numbers)))
#
# if __name__ == "__main__":
#   main()

