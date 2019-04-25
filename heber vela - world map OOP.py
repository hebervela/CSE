class Room(object):
    def __init__(self, name, north=None, south=None, east=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description

class Item(object):
    def __init__(self):


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage

class Character(object):
    def __init__(self, health, weapon, armor, name):
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.name = name

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" %(self.name, target.name, self.weapon))
        target.take_damage(self.weapon.damage)


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []

    def move(self, newlocation):
        """This method moves a character to a new location

        :param newlocation: The variable containing a room object
        :return:
        """
        self.current_location = newlocation


R19A = Room("R19A", 'Parking_lot')
Parking_lot = Room('The parking_lot', None, "R19A")

player = Player(R19A)
directions = ['north', 'south', 'east', 'west']

playing = True

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in directions:
        try:
            # command = 'north'
            room_object_that_we_move_to = getattr(player.current_location, command)

            #NEEDE FOR OPTION 2
            room_var = globals()[room_object_that_we_move_to]

            player.move(room_var)
        except KeyError:
           print("I can't go that way.")
    else:
        print("command not recognized")


# Items
Sword = Weapon("sword", 15)
Sword2 = Weapon("orc sword2", 5)

c1 = Character("orc1", 100, Sword, None)
c2 = Character("orc2", 100, Sword2, None)