
class Phone(object):
    def __init__(self, sound, applications, brightness,):
        self.sound = sound
        self.power = True
        self.home = applications
        self.screen = brightness
        self.duration_of_battery = 100
        self.off = False

    def on(self, time):
        if self.screen:
            if self.duration_of_battery <= 0:
                print("battery has died it needs to charge")
            elif self.duration_of_battery < time:
                print("you run out of battery after using it for %s hours" % self.duration_of_battery)
                self.duration_of_battery = 0
            else:
                print("there's no power!")

    def charge(self) -> object:
        self.duration_of_battery = 100


my_Phone = Phone(100, 100, True)
your_phone = Phone(15, 20, False)


my_Phone.on(100)
my_Phone.charge()

