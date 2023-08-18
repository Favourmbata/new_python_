import collections
list1 = [20,20,30,60,65,75,80,85]
list2 = [42,30,30,80,65,68,88,95]


result = collections.Counter (list1)&collections.Counter(list2)

intersected_list = tuple(result.elements())
print(intersected_list)