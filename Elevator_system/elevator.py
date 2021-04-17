class Elevator():
    def __init__(self):
        self.current_level = 0
        self.max_level = 13
        self.min_level = -2
        self.fan = 0
        self.light = 0
    def move(self, level):
        if level > self.max_level or level < self.min_level:
            print("Invalid level. Level does not exist in building!")
            return
        if level < self.current_level:
            for i in range(self.current_level, level-1, -1):
                print("Reached level",i)
                self.current_level = i
            self.door_open()
        elif level > self.current_level:
            for i in range(self.current_level, level+1):
                print("Reached level",i)
                self.current_level = i
            self.door_open()
        else:
            print("Select a level! You are on same level you selected!")
        return
    def stop(self):
        print("Elevator Stopped!")
        return
    def fan_on_off(self, switch):
        if self.fan != switch:
            self.fan = switch
            if switch == 1:
                print("Fan On!")
            else:
                print("Fan Off!")
        else:
            if switch == 1:
                print("Fan is already On!")
            else:
                print("Fan is already Off!")
        return
    def light_on_off(self, switch):
        if self.light != switch:
            self.light = switch
            if switch == 1:
                print("Light On!")
            else:
                print("Light Off!")
        else:
            if switch == 1:
                print("Light is already On!")
            else:
                print("Light is already Off!")
        return
    def alarm(self):
        print("Alarm is on. Please wait for help!!")
        return
    def door_open(self):
        print("Door opening!")
        self.door_close()

    def door_close(self):
        print("Door closing!")
        return

elev = Elevator()
print("Welcome to the Elevator System!!")
print("There are total 15 level in this buliding, which includes Level 0, 2 basement levels for parking i.e., P1(Level -1) and P2(Level -2)")
print("You are on Level 0")
print("Press button to open door:(Just press Enter)")
input()
elev.door_open()
terminate = 'yes'
while terminate != 'no':
    print("Select from the following:")
    print("1. Select the level you want to go")
    print("2. Fan On")
    print("3. Fan Off")
    print("4. Light On")
    print("5. Light Off")
    print("6. Alarm")
    print("7. Stop")
    choice = eval(input("Enter your choice:"))
    if choice == 1:
        which_level = eval(input("Enter the level you want to go:"))
        elev.move(which_level)
    elif choice == 2:
        elev.fan_on_off(1)
    elif choice == 3:
        elev.fan_on_off(0)
    elif choice == 4:
        elev.light_on_off(1)
    elif choice == 5:
        elev.light_on_off(0)
    elif choice == 6:
        elev.alarm()
    elif choice == 7:
        elev.stop()
    else:
        print("Please enter valid options. Thank you!")
    terminate = input("Do you want to continue?(yes/no):")
print("Thank you for using Elevator System.")