from classes.tile import Tile


class Pit(Tile):
    map_symbol = '\u25CB'

    def __init__(self, row, column, length):
        Tile.__init__(self, row, column, length)
        self.empty = False
        self.spawn_buffer = 2
        self.Map_symbol = Pit.map_symbol