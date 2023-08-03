import operator

dictionary ={1:2,3:4,4:3,2:1,0:0}
print('Original dictionary : ',dictionary)
sorted_dictionary = sorted(dictionary.items(),key=operator.itemgetter(1))
print('dictionary in ascending order by value : ',sorted_dictionary)
sorted_dictionary = dict(sorted(dictionary.items(),key=operator.itemgetter(1),reverse= True))
print('dictionary in descending order by value :',sorted_dictionary)