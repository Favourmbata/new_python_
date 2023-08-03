my_list = [1,2,3,4]
new_list = current = {}
for name in my_list:
    current[name] = {}
    current = current[name]
print(new_list)