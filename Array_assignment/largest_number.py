def largest_number(numbers):
    biggest_number = numbers[0]

    for number in numbers:
        if number > biggest_number:
            biggest_number = number

    return biggest_number


print(largest_number([10, 15, 5, 20, 8, 30, 100, 4]))
