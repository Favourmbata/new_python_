average_score = 0
total = 0
count = 0

score = 0
while score!= -1:
    score = int(input("enter student score "))
    if score == -1:
        print("No more scores")
        break
    total = score+total
    count = count+1
print(total)
print(count)

print(total / count)
