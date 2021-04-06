while True:
    try:
        num1 = input("enter number")
        if (len(num1) == 4):
            print("enter number is four digit only")
            break
    except ValueError:
        print("Enter number with only four digits")