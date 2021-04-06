string = input("Enter an input String:")
dir1 = {}
for i in string:
    if i in dir1:
        continue
    else:
        dir1[i] = 1
print(dir1.keys())