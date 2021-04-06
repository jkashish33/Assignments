def info():
    num = 0
    while True:
        yield num
        num += 1
a= info()
print(a.__next__())
print(a.__next__())
print(a.__next__())
for i in a:
    print(i)