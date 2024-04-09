class Tile:
    def __init__(self, row=1, column=1, length=20):
        self.empty = True
        self.column = column
        self.x_coordinate = self.column + 1
        self.row = row
        self.y_coordinate = length - self.row
        self.coordinates = (self.x_coordinate, self.y_coordinate)
        self.spawn_buffer = 0
        # I think i can use class instead of the symbol
        self.map_symbol = ' '

    def kill(self, world):
        world.board[self.row][self.column] = Tile(self.row, self.column)

    def __str__(self):
        return f"{self.location}"