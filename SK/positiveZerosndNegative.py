
count_positive = 0
count_negative = 0
count_zeros = 0

while True:
    user_input = int(input("Enter the numbers you want:"))


    if user_input > 0:
        count_positive+=1
    elif user_input < 0:
        count_negative+=1
    else:
        count_zeros+=1

    choice = input("Do you want to continue ( yes / no) ?").lower()
    if choice != "yes" :
     if choice != "no":
         break
print("The positive numbers are " + count_positive)
print("The negative numbers are " + count_negative)
print("The zeror are "+ count_zeros)

