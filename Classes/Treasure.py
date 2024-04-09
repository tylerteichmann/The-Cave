from Classes.Tile import Tile

class Treasure(Tile):
    Map_symbol = 'T'

    def __init__(self, row, column, length):
        Tile.__init__(self, row, column, length)
        self.empty = False
        self.spawn_buffer = 2
        self.Map_symbol = Treasure.Map_symbol