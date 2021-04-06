def square(n):
    list1 = []
    for i in range(1,n+1):
        a = i*i
        list1.append(a)
    return(list1)

print(tuple(square(20)))