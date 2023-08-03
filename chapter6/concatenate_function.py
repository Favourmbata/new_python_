values = {1:10,2:20}
values2 = {3:30,4:40}
values3 = {5:50,6:60}
values4 = {}
for d in (values,values2,values3):values4.update(d)
print(values4)