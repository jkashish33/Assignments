from functools import reduce
list1 = [1,2,3,4,5,6,7]
flatten_list = reduce(lambda total, i: 10 * total + i, list1)
print(flatten_list)