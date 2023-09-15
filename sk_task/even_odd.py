# number = [1,2,3,4,5,6,7,8,9]
# for i in number :
#     if i % 2 == 0  :
#         print(f"Numbers of even is {i}")
#     else:
#         print(f"Numbers of odd is {i}")



number = [1,2,3,4,5,6,7,8,9]
count_odd = 0
count_even = 0
for num in  number:
    if num % 2 == 0:
     count_even+=1
    else:
      count_odd+=1
print("Number of even is ",count_even)
print("Number of odd is ",count_odd)
