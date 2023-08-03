scores = [66,90,68,59,76,60,88,81,65,92,85,74]

def is_A_student(score):
    return  score > 80

passing = list(filter(is_A_student,scores))
print(passing)
