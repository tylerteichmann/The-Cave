from classes.tile import Tile


class Wall(Tile):
    map_symbol = '\u25A0'

    def __init__(self, row, column, length):
        Tile.__init__(self, row, column, length)
        self.empty = False
        self.Map_symbol = Wall.map_symbol