class Item(object):
    def __init__(self):


class Room(object):
    def __init__(self, name, north=None, south=None, east=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description


class Character(Item):
    def __init__(self, health, weapon, armor, name):
        super(Character, self).__init__(name)
        self.health = health
        self.weapon = weapon
        self.armor = armor


    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon))
        target.take_damage(self.weapon.damage)

    def damage(self, target):
        self.attck = target
        self.damage = True


class Sword(Item):
    def __init__(self, sword, name, damage=20):
        super(Sword, self).__init__(damage, name)
        self.damage = 20
        self.sword = sword
        self.name = Sword
        self.damage = damage


class InfernoSword(Item):
    def __init__(self, sword, name, damage=40):
        super(InfernoSword, self).__init__(damage, name)
        self.damage = 40
        self.Weapon = sword
        self.name = Sword
        self.damage = damage

