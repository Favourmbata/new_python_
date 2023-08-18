import  time

seconds = int(input("enter an integer for seconds"))

minutes = seconds // 60
remaining_seconds = seconds % 60
print(seconds,"seconds is ",minutes,"minutes and",remaining_seconds,"seconds")
