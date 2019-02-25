class Room(object):
    def __init__(self, name, north=None, south=None, east=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description

# option 1
R19A = Room("R19A")
Parking_lot = Room('The parking Lot', None, R19A)

R19A.north = Parking_lot

# option 2

R19A = Room("R19A", 'Parking_lot')
Parking_lot = Room('The parking_lot',None,"R19A")
