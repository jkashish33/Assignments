class Person:
    age = 0
    def __init__(self, integer):
        if integer < 0:
            print("Age is not valid, setting age to 0")
        else:
            self.age = integer

    def yearPasses(self):
        self.age += 1

    def amIOld(self):
        if self.age == 0 or self.age < 13:
            print("You are young")
        elif self.age >= 13 and self.age <= 19:
            print("You are a teenager")
        else:
            print("You are old")

a= Person(38)
a.amIOld()