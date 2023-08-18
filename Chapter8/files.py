def largest_number():
    maxi = 0
    salespersonCounter = 0
    while salespersonCounter < 10:
        unit_sold = int(input("enter sales person unit"))
        if unit_sold > maxi: maxi = unit_sold
        salespersonCounter += 1
    return maxi


print("the largest number is", largest_number())