employees_name = input("Enter Employee's name->")
hours_worked = float(input("Enter number of hours worked->"))
hourly_pay_rate = float(input("Enter hourly pay rate->"))
month = input("Enter month-> ")
federal_tax_withholding_rate = float(input("Enter federal tax withholding rate->"))
state_tax_withholding_rate = float(input("Enter state tax withholding rate->"))

Gross_pay = (hours_worked * hourly_pay_rate)

federal_withholding = Gross_pay * (federal_tax_withholding_rate /100)
state_withholding = Gross_pay * (state_tax_withholding_rate/100)

net_pay = Gross_pay - federal_withholding - state_withholding

Total_deduction = (Gross_pay - net_pay)
print("***************************************")
print("Employee's name is:", employees_name)
print("Number of hours:$", hours_worked)
print("Hourly pay rate:", hourly_pay_rate)
print("Gross pay: $",Gross_pay)
print("Deductions:$")
print("Federal tax withholding is: $",federal_withholding)
print("State tax withholding: $",state_withholding)
print("Total Deduction$",Total_deduction)
print("Net Pay:$",net_pay)

