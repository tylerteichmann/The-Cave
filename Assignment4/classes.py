class tile:
    def __init__(self, row, column, length):
        self.empty = True
        self.x_coordinate = column + 1
        self.y_coordinate = length - row
        self.coordinates = (self.x_coordinate, self.y_coordinate)
        self.spawn_buffer = 0

    def __str__(self):
        return f"{self.location}"

class Wall(tile):
    def __init__(self, row, column, length):
        tile.__init__(self, row, column, length)
        self.empty = False

class Treasure(tile):
    def __init__(self, row, column, length):
        tile.__init__(self, row, column, length)
        self.empty = False
        self.spawn_buffer = 2

class Pit(tile):
    def __init__(self, row, column, length):
        tile.__init__(self, row, column, length)
        self.empty = False
        self.spawn_buffer = 2

class Monster(tile):
    def __init__(self, row, column, length):
        tile.__init__(self, row, column, length)
        self.empty = False
        self.spawn_buffer = 3

class Hero(tile):
    def __init__(self, row, column, length):
        tile.__init__(self, row, column, length)
        self.empty = False

    def look():
        pass

    def hear():
        pass

    def attack(direction):
        pass

    def move(direction):
        pass
