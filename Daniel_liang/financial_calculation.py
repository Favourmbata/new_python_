sub_total = float(input("enter  a value for sub total : "))
gratuity_rate = float(input("enter a value for gratuity: "))


gratuity = sub_total * gratuity_rate / 100
total = gratuity + sub_total

print(" the gratuity is  $ ",gratuity, "the total is $ ",total)

