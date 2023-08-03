number = {'n1':[2,3,1],'n2':[5,1,2],'n3':[3,2,4]}
sorted_number = {x:sorted(y)for x,y in number.items()}
print(sorted_number)