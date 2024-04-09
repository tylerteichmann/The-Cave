from Classes.Tile import Tile

class Wall(Tile):
    Map_symbol = '\u25A0'

    def __init__(self, row, column, length):
        Tile.__init__(self, row, column, length)
        self.empty = False
        self.Map_symbol = Wall.Map_symbol