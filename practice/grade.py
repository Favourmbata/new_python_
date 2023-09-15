score = int(input("Enter your score:"))

result = " "
if 90 <= score <= 100:
    result = "distinctions"
elif score <= 80 and score < 90:
    result = "excellent"
elif 70 <= score < 80:
    result = "B Grade"
elif score <= 50 and score < 60:
    result = "D Grade"
elif score < 50:
    result = "fail come back next time"

print(result)
