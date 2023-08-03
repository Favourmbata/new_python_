values = {1:10,2:20,3:30,4:40,5:50,6:60}
def is_key_present(x):
    if x in values:
        print('key is present in the dictnary')
    else:
        print('key is not present in the dictionary')
is_key_present(5)
is_key_present(9)
print(values)