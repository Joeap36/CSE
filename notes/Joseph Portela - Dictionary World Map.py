world_map = {
    'WHITE': {
        'NAME': "The White Room",
        'DESCRIPTION': "The room is almost blindingly white, there"
                       "are four passages, each on one side of the"
                       "room. Violet is to the south, scarlet is to"
                       "the east, yellow is to the north, and"
                       "turquoise is to the west.",
        'PATHS': {
            'NORTH': 'YELLOW',
            'EAST': 'SCARLET',
            'SOUTH': 'VIOLET',
            'WEST': 'TURQUOISE'
        }
    },
    'YELLOW': {
        'NAME': "The Yellow Room",
        'DESCRIPTION': "The room is completely yellow. Four exits, one"
                       "on each wall, leave the room. Orange yellow is"
                       "to the north, red is to the east, white is to"
                       "the south, and yellow green is to the west.",
        'PATHS': {
            'NORTH': 'ORANGE_YELLOW',
            'EAST': 'RED',
            'SOUTH': 'WHITE',
            'WEST': 'YELLOW_GREEN'
        }
    },
    'ORANGE_YELLOW': {
        'NAME': "The Orange Yellow Room",
        'DESCRIPTION': "The room is orange yellow. Four exits, one"
                       "on each wall, leave the room. A strange,"
                       "portal-like door is to the north, orange is"
                       "to the east, yellow is to the south, and"
                       "lemon yellow is to the west.",
        'PATHS': {
            'NORTH': 'VWORP',
            'EAST': 'ORANGE',
            'SOUTH': 'YELLOW',
            'WEST': 'LEMON_YELLOW'
        }
    },
    'SCARLET': {
        'NAME': "The Scarlet Room",
        'DESCRIPTION': "The room is completely scarlet. Four exits,"
                       "one on each wall, leave the room. red is to"
                       "the north, crimson is to the east, purple is"
                       "to the south, and white is to the west.",
        'PATHS': {
            'NORTH': 'RED',
            'EAST': 'CRIMSON',
            'SOUTH': 'PURPLE',
            'WEST': 'WHITE'
        }
    },
    'CRIMSON': {
        'NAME': "The Crimson Room",
        'DESCRIPTION': "The room is completely crimson. Four exits, one"
                       "on each wall, leave the room. Scarlet red is"
                       "to the north, a strange, portal-like door is"
                       "to the east, magenta is to the south, and"
                       "scarlet is to the west.",
        'PATHS': {
            'NORTH': 'SCARLET_RED',
            'EAST': 'VWORP',
            'SOUTH': 'MAGENTA',
            'WEST': 'SCARLET'
        }
    },
    'VIOLET': {
        'NAME': "The Violet Room",
        'DESCRIPTION': "The room is completely violet. Four exits, one"
                       "on each wall, leave the room. White is to the"
                       "north, purple is to the east, blue violet is to"
                       "the south, and cyan blue is to the west.",
        'PATHS':
    }
}

# Controller
playing = True
current_node = world_map['WHITE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN', 'VWORP']

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input("> ")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command Not Found")
