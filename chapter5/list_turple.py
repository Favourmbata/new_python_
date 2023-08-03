def test(n):
     return n ** 2
my_list = {1,2,3,4,5,6,7,8,9,10}

print(list(map(test,my_list)))




ans = [m for m in my_list if m % 2 == 0]
print(ans)