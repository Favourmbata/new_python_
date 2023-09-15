def multiple(number, division):
    remainder = number % division
    return remainder == 0


print("is 1024 a multiple of 4? ", multiple(1024, 4))
print("is 10 a multiple of 2? ", multiple(10, 2))
