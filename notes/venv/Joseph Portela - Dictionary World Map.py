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
        'DESCRIPTION': ""
    }
}

# Controller
playing = True
current_node = world_map['WHITE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

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
