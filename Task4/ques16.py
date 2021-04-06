def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

#Output: 2.


def a():
    try:
        f(x, 4)
    finally:
       print('after f')
    print('after f?')
a()

#Output: It prints finally code and the gives error.
#after f
#Error: name 'f' is not defined