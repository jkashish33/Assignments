def showNumbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            print(i, end=" ")
            print("EVEN")
        else:
            print(i, end=" ")
            print("ODD")

showNumbers(3)