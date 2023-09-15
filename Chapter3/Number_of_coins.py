purchase_price = int(input("Enter the  purchase price of an item"))
change_due  = 1.00 - purchase_price
change_due_cent = int(change_due * 100)

quarters = (change_due // 25)
change_due_cent %= 25

dimes = change_due_cent // 10
change_due_cent %= 25

nickels = change_due_cent // 5
change_due %= 5
pennies = change_due_cent


print("Your change is:")
if quarters > 0:
    print(f"{quarters} {'quarter' if quarters == 1 else 'quarters'}")
if dimes > 0:
    print(f"{dimes} {'dime' if dimes == 1 else 'dimes'}")
if nickels > 0:
    print(f"{nickels} {'nickel' if nickels == 1 else 'nickels'}")
if pennies > 0:
    print(f"{pennies} {'penny' if pennies == 1 else 'pennies'}")