def div(n):
    res = []
    for i in range(len(n)):
        if (i % 3 != 0) & (i % 7 == 0):
            res.append(i)
    return res

n = input("Enter a range:")
list1 = range(1, int(n))
a = (list(div(list1)))
print(a)