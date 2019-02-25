world_map = {
    'LIVING ROOM 1': {
        'NAME':"Living room",
        'DESCRIPTION': "This is the livingroom the main room of the house.",
        'PATHS': {
            'SOUTH': "Dining_Room",
}
    },
    'DINING ROOM': {
        'NAME':"Dining Room",
        'DESCRIPTION':"This is the dining room, there is food on the table.",
        'PAHTS': {
            'EAST': "Kitchen",
            'WEST': "Guest_Room",
        }
    },
    'KITCHEN': {
        'NAME':"Kitchen",
        'DESCRIPTION':"This is the kitchen, there is a lot of knives.",
        'PATHS': {
            'WEST': "Dining_Room",
        }
    },
    'GUEST ROOM': {
        'NAME':"Guest_Room",
        'DESCRIPTION':"This is the guest room, theres a couch and a candle.",
        'PATHS': {
            'EAST':"Dining_Room",
            'NORTH':"Bed_Room",
            'SOUTH':"Yard",
            'WEST':"Living_Room",
        }
    },
    'ROOM5': {
        'NAME':"Bed_Room",
        'DESCRIPTION':"This is a bedroom, there's a vanity full of jewlery looks like a girl room.",
        'PATHS': {
            'WEST':"Room_4",
            'SOUTH':"Guest_Room",
        }
    },
    'YARD1': {
        'NAME':'Yard',
        'DESCRIPTION':'This the yard, there is a shovel next to you',
        'PATHS': {
            'NORTH':"Guest_Room",
        }
    },
    'LIVING ROOM2': {
        'NAME':"Living Room",
        'DESCRIPTION': "This is the second living room, its empty",
        'PATHS': {
            'EAST': "Guest Room",
            'SOUTH': "Masters bedroom",
            'WEST': "Toy Room",
        }
    },
}
