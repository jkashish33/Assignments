class shape:
    def __init__(self):
        pass

    def area(self):
        print(0)


class square(shape):
    def __init__(self, length):
        self.length = length
        super(square, self).__init__()

    def area(self):
        a = (self.length * self.length)
        print('The area of a square with a side length of %f is %f' % (self.length, a))


s = square(4)
s.area()