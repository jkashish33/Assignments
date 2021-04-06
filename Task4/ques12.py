def divide_num(n):
    try:
       n = n/0
    except ZeroDivisionError:
        print("Divisor can't be zero")
divide_num(5)