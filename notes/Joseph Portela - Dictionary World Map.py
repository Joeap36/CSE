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
        'PATHS': {
            'NORTH': 'WHITE',
            'EAST': 'PURPLE',
            'SOUTH': 'BLUE_VIOLET',
            'WEST': 'CYAN_BLUE'
        }
    },
    'BLUE_VIOLET': {
        'NAME': "The Blue Violet Room",
        'DESCRIPTION': "The room is completely blue violet. Four exits,"
                       "one on each wall, leave the room. Violet is to"
                       "the north, purple violet is to the east, a strange,"
                       " portal-like door is to the south, and blue is to"
                       "the west.",
        'PATHS': {
            'NORTH': 'VIOLET',
            'EAST': 'PURPLE_VIOLET',
            'SOUTH': 'VWORP',
            'WEST': 'BLUE'
        }
    },
    'TURQUOISE': {
        'NAME': "The Turquoise Room",
        'DESCRIPTION': "The room is completely turquoise. Four exits, one"
                       "on each wall, leave the room. Yellow green is to"
                       "the north, white is to the east, cyan blue is to"
                       "the south, and blueish green is to the west.",
        'PATHS': {
            'NORTH': 'YELLOW_GREEN',
            'EAST': 'WHITE',
            'SOUTH': 'CYAN_BLUE',
            'WEST': 'BLUEISH_GREEN'
        }
    },
    'RED': {
        'NAME': "The Red Room",
        'DESCRIPTION': "The room is completely red. Four exits, one"
                       "on each wall, leave the room. Orange is to the"
                       "north, scarlet red is to the east, scarlet is"
                       "to the south, and yellow is to the west.",
        'PATHS': {
            'NORTH': 'ORANGE',
            'EAST': 'SCARLET_RED',
            'SOUTH': 'SCARLET',
            'WEST': 'YELLOW'
        }
    },
    'ORANGE_RED': {
        'NAME': "The Orange Red Room",
        'DESCRIPTION': "The room is completely orange red. Two exits"
                       "leave the room. Scarlet red is to the south"
                       "and orange is to the west.",
        'PATHS': {
            'SOUTH': 'SCARLET_RED',
            'WEST': 'ORANGE'
        }
    },
    'PURPLE': {
        'NAME': "The Purple Room",
        'DESCRIPTION': "The room is completely purple. Four exits, one"
                       "on each wall, leave the room. Scarlet is to the"
                       "north, magenta is to the east, purple violet is"
                       "to the south, and violet is to the west.",
        'PATHS': {
            'NORTH': 'SCARLET',
            'EAST': 'MAGENTA',
            'SOUTH': 'PURPLE_VIOLET',
            'WEST': 'VIOLET'
        }
    },
    'PURPLE_MAGENTA': {
        'NAME': "The Purple Magenta Room",
        'DESCRIPTION': "The room is completely violet. Two exits"
                       "leave the room. Magenta is to the north"
                       "and purple violet is to the west.",
        'PATHS': {
            'NORTH': 'MAGENTA',
            'WEST': 'PURPLE_VIOLET'
        }
    },
    'CYAN_BLUE': {
        'NAME': "The Cyan Blue Room",
        'DESCRIPTION': "The room is completely cyan blue. Four exits,"
                       "one on each wall, leave the room. Turquoise"
                       "is to the north, violet is to the east, blue"
                       "is to the south, and greenish cyan is to the"
                       "west.",
        'PATHS': {
            'NORTH': 'TURQUOISE',
            'EAST': 'VIOLET',
            'SOUTH': 'BLUE',
            'WEST': 'GREENISH_CYAN'
        }
    },
    'BLUEISH_CYAN': {
        'NAME': "The Blueish Cyan Room",
        'DESCRIPTION': "The room is completely blueish cyan. Two"
                       "exits leave the room. Greenish cyan is to"
                       "the north, and blue is to the east.",
        'PATHS': {
            'NORTH': 'GREENISH_CYAN',
            'EAST': 'BLUE'
        }
    },
    'YELLOW_GREEN': {
        'NAME': "The Yellow Green Room",
        'DESCRIPTION': "The room is completely yellow green. Four exits,"
                       "one on each wall, leave the room. Lemon yellow is"
                       "to the north, yellow is to the east, turquoise is"
                       "to the south, and green is to the west.",
        'PATHS': {
            'NORTH': 'LEMON_YELLOW',
            'EAST': 'YELLOW',
            'SOUTH': 'TURQUOISE',
            'WEST': 'GREEN'
        }
    },
    'SAP_GREEN': {
        'NAME': "The Sap Green Room",
        'DESCRIPTION': "The room is completely sap green. Two exits"
                       "leave the room. Lemon yellow is to the east, and"
                       "green is to the south.",
        'PATHS': {
            'EAST': 'LEMON_YELLOW',
            'SOUTH': 'GREEN'
        }
    },
    'ORANGE': {
        'NAME': "The Orange Room",
        'DESCRIPTION': "The room is completely orange. Three exits"
                       "leave the room. Orange red is to the east, red is"
                       "to the south, and orange yellow is to the west.",
        'PATHS': {
            'EAST': 'ORANGE_RED',
            'SOUTH': 'RED',
            'WEST': 'ORANGE_YELLOW'
        }
    },
    'SCARLET_RED': {
        'NAME': "The Scarlet Red Room",
        'DESCRIPTION': "The room is completely scarlet red. Three exits"
                       "leave the room. Orange red is to the north, crimson"
                       "is to the south, and red is to the west.",
        'PATHS': {
            'NORTH': 'ORANGE_RED',
            'SOUTH': 'CRIMSON',
            'WEST': 'RED'
        }
    },
    'MAGENTA': {
        'NAME': "The Magenta Room",
        'DESCRIPTION': "The room is completely magenta. Three exits"
                       "leave the room. Crimson is to the north, purple"
                       "magenta is to the south, and purple is to the"
                       "west.",
        'PATHS': {
            'NORTH': 'CRIMSON',
            'SOUTH': 'PURPLE_MAGENTA',
            'WEST': 'PURPLE'
        }
    },
    'PURPLE_VIOLET': {
        'NAME': "The Purple Violet Room",
        'DESCRIPTION': "The room is completely purple violet. Three exits"
                       "leave the room. Purple is to the north, purple"
                       "magenta is to the east, and blue violet is to the"
                       "west.",
        'PATHS': {
            'NORTH': 'PURPLE',
            'EAST': 'PURPLE_MAGENTA',
            'WEST': 'BLUE_VIOLET'
        }
    },
    'BLUE': {
        'NAME': "The Blue Room",
        'DESCRIPTION': "The room is completely blue. Three exits leave the"
                       "room. Cyan Blue is to the north, blue violet is to"
                       "the east, and blueish cyan is to the west.",
        'PATHS': {
            'NORTH': 'CYAN_BLUE',
            'EAST': 'BLUE_VIOLET',
            'WEST': 'BLUEISH_CYAN'
        }
    },
    'GREENISH_CYAN': {
        'NAME': "The Greenish Cyan Room",
        'DESCRIPTION': "The room is completely greenish cyan. Three exits"
                       "leave the room. Blueish green is to the north, cyan"
                       "blue is to the east, and blueish cyan is to the"
                       "south.",
        'PATHS': {
            'NORTH': 'BLUEISH_GREEN',
            'EAST': 'CYAN_BLUE',
            'SOUTH': 'BLUEISH_CYAN'
        }
    },
    'GREEN': {
        'NAME': "The Green Room",
        'DESCRIPTION': "The room is completely green. Three exits leave"
                       "the room. Sap green is to the north, yellow"
                       "green is to the east, and blueish green is to the"
                       "south.",
        'PATHS': {
            'NORTH': 'SAP_GREEN',
            'EAST': 'YELLOW_GREEN',
            'SOUTH': 'BLUEISH_GREEN'
        }
    },
    'LEMON_YELLOW': {
        'NAME': "The Lemon Yellow Room",
        'DESCRIPTION': "The room is completely lemon yellow. Three exits"
                       "leave the room. Orange yellow is to the east,"
                       "yellow green is to the south, and sap green is to"
                       "the west.",
        'PATHS': {
            'EAST': 'ORANGE_YELLOW',
            'SOUTH': 'YELLOW_GREEN',
            'WEST': 'SAP_GREEN'
        }
    },
    'VWORP': {
        'NAME': "Vworp",
        'DESCRIPTION': "Vworpvworpvworpvworpvworpvworpvworpvworpvworpvworp"
                       "vworpvworpvworpvworpvworpvworpvworpvworpvworpvworp"
                       "vworpvworpvworpvworpvworpvworpvworpvworpvworpvworp",
        'PATHS': {
            'VWORP': 'WHITE'
        }
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
