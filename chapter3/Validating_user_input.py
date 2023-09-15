passes = 0
failures = 0
counter = 0

while counter <= 10:
    result = int(input("Enter  result (1 = pass,2 = fail) :"))
    while result != 1 and result != 2:
        print("Invalid input. Please enter 1  for pass or 2 for fail->")
        result = int(input("Enter result ( 1= pass,2= fail):"))
    if result == 1:
        passes = passes + 1
    else:
        failures = failures + 1

    print('passed:', passes)
    print('failures', failures)

