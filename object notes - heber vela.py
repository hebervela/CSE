import Special_Random


class WaterGun(object):
    def __init__(self, capacity, distance=30, stock=False):
        self.capacity = capacity
        self.range = distance
        self.trigger = True
        self.stock = stock
        self.duration_of_pressure = 5

    def shoot(self, time):
        if self.trigger:
            if self.duration_of_pressure <= 0:
                print("There's no pressure!")
            elif self.duration_of_pressure < time:
                print("You runout of pressure after firing for %s seconds" % self.duration_of_pressure)
                self.duration_of_pressure = 0
            else:
                print("you shoot for %s seconds" % time)
                self.duration_of_pressure -= time
        else:
            print("There's no trigger!")

    def pump_it_up(self):
        self.duration_of_pressure = 5


# initiate the objects
my_Water_Gun = WaterGun(5.2, 40, True)
your_Water_Gun = WaterGun(1.0, 1, False)
wiebe_Water_Gun = WaterGun(9999999999,99999999999999999999, True)
yahir_Water_Gun = WaterGun(0.1)

# do stuff with the object
my_Water_Gun.shoot(5)
my_Water_Gun.pump_it_up()
my_Water_Gun.shoot(1)

print(Special_Random.RandomWiebe.special_random())