ls = [8,7,4,3,9,2, 1]
def even_number(lst):
  new_lst = []
  for number in lst:
    if number % 2 == 0 :
     new_lst.append(number)
    return new_lst
result = [i for i in ls if i % 2 == 0]
print(result)