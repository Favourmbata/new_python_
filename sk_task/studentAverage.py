
#
# total = 0
# count = 1
# while count<= 10:
#     score = float(input("Enter 10 scores "))
#     total += score
#     count += 1
# average = total /count
# print("the total sum is",total)
# print("The score is ", average)


count = 1
total = 0
# while count <= 10:
#     score = int(input("Enter student score"))
#     print(score)
#     count = count +1
#     total += score
# average = total /count
# print(f'the total of scores by the student is {total}\n The average score is {average}')


# while True:
#     score = int(input("Enter score or -1 to quit:"))
#     if score == -1:
#         break
#     count = count +1
#     total += score
# average = total/count
# print(f'The total of score is:{total}\n The average is {average}')

score = int(input("Enter a student score or -1 to stop:"))
while score != -1:

    total += score
    count += 1
    score = int(input("Enter student score or -1 to quit:"))
average = total / count
print(total)
print(average)

