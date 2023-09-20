# user_percent = float(input("Enter your investment"))
# amount_invested = float(input("Enter amount invested"))
# roy = 0.10
# for year in range(1, 31):
#     investment = user_percent * (roy + 1) ** year
#     print(f"Your Roy is ${amount_invested}: year{year}:Your investment is {investment:.2f}")

deposit = float(input("Enter your amount:"))

for i in range(1,31):
    roi = deposit * 0.10
new_amount = deposit + roi
deposit = new_amount
print(f'Your Roi is ${roi},Your investment is now ${new_amount:.2f} in Year{i}')