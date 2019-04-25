world_map = {
    'LIVING ROOM 1': {
        'NAME': "Living room",
        'DESCRIPTION': "This is the living room the main room of the house.",
        'PATHS': {
            'SOUTH': "DINING ROOM",
}
    },
    'DINING ROOM': {
        'NAME': "Dining Room",
        'DESCRIPTION': "This is the dining room, there is food on the table.",
        'PATHS': {
            'EAST': "KITCHEN",
            'WEST': "GUEST ROOM",
        }
    },
    'KITCHEN': {
        'NAME': "Kitchen",
        'DESCRIPTION': "This is the kitchen, there is a lot of knives.",
        'PATHS': {
            'WEST': "DINING ROOM",
        }
    },
    'GUEST ROOM': {
        'NAME': "Guest_Room",
        'DESCRIPTION': "This is the guest room, theres a couch and a candle.",
        'PATHS': {
            'EAST': "DINING ROOM",
            'NORTH': "ROOM5",
            'SOUTH': "YARD1",
            'WEST': "LIVING ROOM 1",
        }
    },
    'ROOM5': {
        'NAME': "Girls_Room",
        'DESCRIPTION': "This is a bedroom, there's a vanity full of jewlery looks like a girl room.",
        'PATHS': {
            'WEST': "ROOM4",
            'SOUTH': "GUEST ROOM",
        }
    },
    'YARD1': {
        'NAME': 'Yard',
        'DESCRIPTION': 'This the yard, there is a shovel next to you',
        'PATHS': {
            'NORTH': "GUEST ROOM",
        }
    },
    'LIVING ROOM2': {
        'NAME': "Living Room",
        'DESCRIPTION': "This is the second living room, its empty",
        'PATHS': {
            'EAST': "GUEST ROOM",
            'SOUTH': "MASTERS BEDROOM",
            'WEST': "ROOM1",
        }
    },
    'ROOM4': {
        'NAME': "Boys_room",
        'DESCRIPTION': "The wall is blue, this looks like the boys room.",
        'PATHS': {
            'EAST': "ROOM5",
            'WEST': "ROOM3"
        }
    },
    'ROOM3': {
        'NAME': "Toy_Room",
        'DESCRIPTION': "There is a lot of toys fo boys and girls looks like a toy room.",
        'PATHS': {
            'WEST': "BATHROOM1",
            'EAST': "ROOM4",
            'SOUTH': "ROOM1"
        }
    },
    'BATHROOM1': {
        'NAME': "Bath_Room",
        'DESCRIPTIONS': "The shower was left on, there is a knife on the counter of the sink",
        'PATHS': {
            'EAST': "ROOM3"
        }
    },
    'ROOM1': {
        'NAME': "Empty_Room",
        'DESCRIPTION': "This room is empty there is nothing in it.",
        'PATHS': {
            'NORTH': "ROOM3",
            'EAST': "LIVING ROOM2",
            'SOUTH': "BATHROOM2"
        }
    },
    'BATHROOM2': {
        'NAME': "Bathroom",
        'DESCRIPTION': "This is the bathroom, its the closest to the masters bedroom",
        'PATHS': {
            'NORTH': "ROOM1",
            'EAST': "MASTERS BEDROOM",
            'SOUTH': "ROOM2"
}
    },
    'MASTERS BEDROOM': {
        'NAME': "Masters Bed Room",
        'DESCRIPTION': "This is the biggest room in the house.",
        'PATHS': {
            'NORTH': "LIVING ROOM2",
            'WEST': "BATHROOM2"
        }
    },
    'ROOM2': {
        'NAME': "Masters Bed Room",
        'DESCRIPTION': "This room is very filthy and needs a lot of cleaning.",
        'PATHS': {
            'NORTH': "BATHROOM2"
        }
    },
    'YARD2': {
        'NAME': "Yard",
        'DESCRIPTION': "This is the second yard in the house, they have a dog but i cant get to it.",
        'PATHS': {
            'NORTH': "MASTERS BEDROOM"
        }
    }
}


# Controller
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
short_directions = ('n','s','e','w','u','d')
current_node = world_map["LIVING ROOM 1"]  # This is your current location
playing = True

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")

    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")
