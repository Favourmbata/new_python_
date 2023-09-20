initial_investment = float(input("enter amount invested"))
annual_rate = float(input("Enter rate->"))

for year in range(1,31):
    amount = initial_investment * (1 + annual_rate) ** year
    print(f"year{year}:${amount:.2f}")
