d = {1:2,2:4,3:6,4:8}
d.pop(3)
print(d)






x = 5
print(eval('x^3'))


x = 'print(55)'
eval(x)


x = 55
print(eval('x^5'))





def test(x):
    x[0]=['abc']
    x[1]=['xyz']
    return id(x)
y = ['abc','xyz']
print(id(y) ==test(y))