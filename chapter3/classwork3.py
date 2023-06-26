for x in range(0,20,1):
    print(x)





for i in range(-1, 5,2):
    print(i,end=", ")



for j in range(-1,5):
    print(j,end=", ")



for k in[1, 3,5,7,9]:
    x = k**2 - (k-1)*(k+1)
    print(x,end=",")

for number in range(100):
    if number == 10:
        break
    print(number,end=' ')

i = 0
while i <= 9:
    if i % 2 == 0:
     print(i)
     i += 1