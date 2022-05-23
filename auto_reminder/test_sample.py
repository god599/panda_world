
list1 = ['abc','bcd','efg']
list2 = ['abc','bcde','efg']

list3 = set(list2).difference(set(list1))
print(list3)
