def split_list(lst,n):
    return [lst[i:i +n]for  i in range(0,len(lst),n)]

word = ['a','b','c','d','e','f','g','h','i','j','k''l','m','n']
n = 3

small_bit = split_list(word,n)
print(small_bit)