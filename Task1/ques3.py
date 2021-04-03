# Swapping with third variable
a, b = 1, 2
temp = a
a = b
b = temp
print(a, b)

#Swapping without third variable
a, b = 1, 2
a = a + b
b = a - b
a = a - b
print(a, b)