import math

input_values = input("Enter the values in a comma-separated sequence:")
split_values = input_values.split(',')
C = 50
H = 30

for i in split_values:
    D = int(i)
    Q = math.sqrt((2 * C * D) / H)
    print("For D Value of {} result is {}".format(D, Q))