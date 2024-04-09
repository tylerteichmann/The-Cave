from Classes.Tile import Tile

class Monster(Tile):
    Map_symbol = '\u25C6'

    def __init__(self, row, column, length):
        Tile.__init__(self, row, column, length)
        self.empty = False
        self.spawn_buffer = 3
        self.Map_symbol = Monster.Map_symbol