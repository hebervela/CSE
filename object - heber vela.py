class Dog(object):
    def __init__(self, run=3, bark=5, wag=100, turn=180, eat=6):
        self.legs = run
        self.mouth = bark
        self.tail = wag
        self.head = turn
        self.mouth = eat
        self.duration_of_pressure = 5

        def shoot(self, time):
            if self.legs:
                if self.duration_of_pressure <= 0:
                    print("dog has stopped running!")
                elif self.duration_of_pressure < time:
                    print("dog got tired after %s seconds" % self.duration_of_pressure)
                    self.duration_of_pressure = 0
                else:
                    print("dog runs for %s seconds" % time)
                    self.duration_of_pressure -= time
            else:
                print("There's no energy!")

        def Run_it_up(self):
            self.duration_of_pressure = 5