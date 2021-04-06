res = []
for i in range(1, 31):
    if i <= 5 or i > 25:
        res.append(i*i)
print(res)