string = input("Enter String:")

# camel case
output = ''.join(x for x in string.title() if x.isalnum())
print(output)

#Snake case
res = [string[0].lower()]
for i in string[1:]:
    if i in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        res.append('_')
        res.append(i.lower())
    else:
        res.append(i)
print(res)
print(''.join(res))