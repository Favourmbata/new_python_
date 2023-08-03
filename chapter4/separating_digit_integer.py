def space():
    number = 42339

    firstNumber = number // 10000

    secondRemainder = number % 10000
    secondNumber = secondRemainder // 1000

    ThirdRemainder = number % 1000
    ThirdNumber = ThirdRemainder // 100

    fourthRemainder = number % 100
    fourthNumber = fourthRemainder // 10

    fifthRemainder = number % 10
    fifthNumber = fifthRemainder

    print(firstNumber, secondNumber, ThirdNumber, fourthNumber, fifthNumber, end=" ")


if __name__ == '__main__':
    space()
