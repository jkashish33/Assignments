class Time():
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add_time(t1, t2):
        hours = int((t1.minutes + t2.minutes) / 60)

        minutes = t1.minutes + t2.minutes

        if (minutes > 60):
            minutes = (t1.minutes + t2.minutes) % 60

        hours += t1.hours + t2.hours
        newtime = Time(hours, minutes)
        return newtime

    def display_time(self):
        print("time in hours:", self.hours, 'hours', self.minutes, 'minutes')

    def display_mins(self):
        print("time in totalmins:", (self.hours * 60) + self.minutes, 'minutes')

a = Time(2, 50)
b = Time(1, 20)
c = Time.add_time(a, b)
c.display_time()
c.display_mins()