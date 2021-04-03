print("Select from the following:")
print("1: Addition")
print("2: Subtaction")
print("3: Division")
print("4: Multiplication")
print("5: Average")

option = int(input())

if option == 1 or option == 2 or option == 3 or option == 4:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
elif option == 5:
    first = int(input("Enter a number:"))
    second = int(input("Enter a number:"))
if option == 1:
    res = num1 + num2
    if res >= 0:
        print(res)
    else:
        print("NEGATIVE")
elif option == 2:
    res = num1 - num2
    if res >= 0:
        print(res)
    else:
        print("NEGATIVE")
elif option == 3:
    if num2 == 0:
        print("Zero not aloowed in divisor.")
    else:
        res = num1 / num2
        if res >= 0:
            print(res)
        else:
            print("NEGATIVE")
elif option == 4:
    res = num1 * num2
    if res >= 0:
        print(res)
    else:
        print("NEGATIVE")
elif option == 5:
    res = (first + second)/2
    if res >= 0:
        print(res)
    else:
        print("NEGATIVE")




