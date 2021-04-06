def sum_list(list3):
    return sum(list3)

def multiply_list(list3):
    temp = 1
    for i in list3:
        temp = temp * i
    return temp

list3 = [1, 2.5, 3, 4.25, 6, 7, 9.5]
print("Sum of list is:",sum_list(list3))
print("Multiplication of list is:",multiply_list(list3))