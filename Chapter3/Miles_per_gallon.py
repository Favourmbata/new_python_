while True:
    gallons_used = float(input("Enter the gallons used(-1 to end):"))
    if gallons_used == -1:
        break
    miles_driven = float(input("Enter miles driven:"))

    total_miles_diven = miles_driven / gallons_used
    print("The overall average miles is $",total_miles_diven)


