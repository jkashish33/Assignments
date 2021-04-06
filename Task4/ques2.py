string = input("Enter input string:")
upper, lower = 0, 0
if string.isalpha():
    for i in string:
        if i in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            upper += 1
        else:
            lower += 1
print("No. of Uppercase characters:", upper)
print("No. of Lowercase characters:", lower)