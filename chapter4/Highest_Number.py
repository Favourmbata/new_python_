def highest_number(num1, num2, num3, num4):
    maximum = num1
    if num2 > maximum:
        maximum = num2
    if num3 > maximum:
        maximum = num3
    if num4 > maximum:
        maximum = num4
    print(maximum)

    minimum = num1
    if num2 < minimum:
        minimum = num2
    if num3 < minimum:
        minimum = num3
    if num4 < minimum:
        minimum = num4
    print(minimum)


highest_number(300, 10, 116, 5)


