price = float(input("Enter price for an item->"))
name_of_item = input("Enter name of item->")
credit_score_status = input("does he/she have good credit score (yes/no):")

if credit_score_status == "yes":
    discount = 0.10
    down_payment_percentage = 0.10
else:
    discount = 0
    down_payment_percentage = 0.25



discount_price = price - (price * discount)
down_payment_amount = discount_price * down_payment_percentage
remaining_balance = discount_price - down_payment_amount

print("******************************************************")
print("invoice")
print("***********************")
print("Name of item:", name_of_item)
print("price is: $", price)
print("discount of items:$", discount * 100, "%")
print("downpayent percentage:$",down_payment_percentage * 100,"%")
print("deposit:$", down_payment_amount)
print("The remaining balance:$", remaining_balance)
print("****************************************************************")

