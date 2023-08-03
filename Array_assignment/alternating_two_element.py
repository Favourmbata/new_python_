
list1 = ["a,b,c"]
list2 = [1,2,3]
def combine(list1,list2):
   new = []
   for i in range(len(list1)):
     new.append(list1[i])
     new.append(list2[i])
   return new
print(combine(list1,list2))



