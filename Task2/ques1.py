a = eval(input("Enter a number:"))
if a%3 == 0 and a%5==0:
    print("Consultadd - Python Training")
elif a%5 == 0:
    print("Python Training")
elif a%3==0:
    print("Consultadd")
elif a.isdigit():
    print("Number is not divisible by 3 or 5")
else:
    print("Enter valid input number")
