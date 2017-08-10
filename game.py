import locations


class Game:
    def __init__(self):
        self.inventory = []
        self.location = locations.START

    def step(self, direction):
        self.location = self.location.doors[direction]
        self.location.describe()

    def look(self):
        self.location.describe()

    def show_inventory(self):
        print 'You are carrying:'
        for i in self.inventory:
            print '\t', i

    def take(self, item):
        self.inventory.append(self.location.release_item(item))

    def drop(self, item):
        if item not in self.inventory:
            return
        self.location.gain_item(item)


if __name__ == '__main__':
    game = Game()

    game.location.describe()
    full_command = raw_input('What do? ')
    while full_command != 'EXIT':
        fields = full_command.split()
        command = fields[0].lower()
        if command == 'go':
            direction = fields[1].upper()
            game.step(direction)
        elif command in ['i', 'inventory']:
            game.show_inventory()
        elif command in ['l', 'look']:
            game.look()
        elif command in ['t', 'take']:
            item = fields[1].lower()
            game.take(item)
        elif command in ['d', 'drop']:
            item = fields[1].lower()
            game.drop(item)
        else:
            print 'Unknown command.'
        full_command = raw_input('What do? ')
