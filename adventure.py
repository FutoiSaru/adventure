from data import locations

directions = {
    'west': (-1, 0),
    'east': (1, 0),
    'north': (0, -1),
    'south': (0, 1),
}

inventory = []
position = (0, 0)

while True:
    location = locations[position]
    print 'You are at the %s - %s\nThere is %s on the floor' % (location[0], location[1], location[2])

    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible_location = locations.get(possible_position)
        if possible_location:
            print 'To the %s is a %s' % (k, possible_location[0])
            valid_directions[k] = possible_position

    direction = raw_input('Choose a direction or type a command (pickup or inv):\n')
    new_position = valid_directions.get(direction)

    if new_position:
        position = valid_directions[direction]
    elif direction == 'pickup':
        if location[2] == 'nothing':
            print 'There is nothing to pickup'
        else:
            inventory.append(location[2])
            print 'you picked up %s' % location[2]
            location[2] = 'nothing'
    elif direction == 'inv':
        print 'You have %s' % inventory
    else:
        print "You can't go that way"