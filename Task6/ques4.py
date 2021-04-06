input_str ="Consultadd Training"
def reverse_str(input_str):
    for i in range(len(input_str)-1, -1, -1):
        yield input_str[i]

a = reverse_str(input_str)
print(a.__next__())
print(a.__next__())
print(a.__next__())

for i in a:
    print(i)