list5 = [1, 2.5, 3, 4.25, 6, 7, 9.5]
res = []
res = list(x for x in list5 if x%2!=0)
# for i in list5:
#     if i%2 != 0:
#         res.append(i)
print(res)