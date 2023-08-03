
from art import logo


def calculator():
    print(logo)

def add(n1,n2):
    return n1 + n2


def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return  n1 * n2

def Divide(n1,n2):
    return  n1 / n2

operations = {

    "+": add,
    "-": subtract,
    "*": multiply,
    "/": Divide
}
num1 = int(input("what's the first number?:"))
for symbol in operations:
    print(symbol)
should_continue = True


while should_continue:
 operations_symbol = input("pick an operation from the line above: ")
num2 = int(input("what is the second number?: "))
calculation_function = operations[operations_symbol]
first_answer = calculation_function(num1,num2)


print(f"{num1}{operations_symbol}{num2} = {first_answer}")

operations_symbol = input("pick another operations: ")
num3 = int(input("what is the next number?: "))
calculation_function = operations[operations_symbol]
answer = calculation_function(calculation_function(num1,num2),num3)

print(f"{first_answer}{operations_symbol}{num3} = {answer}")
