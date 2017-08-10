class Location:
    def __init__(self, name, description, doors, occupants):
        self.name = name
        self.description = description
        self.occupants = occupants
        self.doors = doors

    def describe(self):
        print self.name
        print self.description
        print 'Around you, you see:'
        for item in self.occupants:
            print '\t', item
        print 'You can go: '
        for direction in self.doors:
            print direction,
        print

    def release_item(self, item):
        if item in self.occupants:
            self.occupants.remove(item)
            return item
        return None

    def gain_item(self, item):
        self.occupants.append(item)


START = Location('Bedroom', 'Your childhood bedroom.', {}, ['teddy', 'bed'])
HALL = Location('Hall', 'The hallway.', {'S': START}, [])
YARD = Location('Backyard', 'The backyard of your house.', {'W': START}, [])
START.doors['N'] = HALL
START.doors['E'] = YARD
