import random

class Map:
    def __init__(self, Map_file):
        self.grid = list()
        self.import_Map(Map_file)

    def import_Map(self, Map_file):
        with open(Map_file, "r") as new_Map:
            for line in new_Map:
                line = line.replace(" ", "")
                line = line.replace("\n", "")
                self.grid.append(list(line))

    def update_Map(self, World):

        for row in World.board:
            for Tile in row:
                self.grid[Tile.row][Tile.column] = Tile.Map_symbol
        
        self.export_Map()

    def export_Map(self):
        with open("current_Map.txt", "w", encoding="UTF-8") as updated_Map:
            for line in self.grid:
                updated_Map.write(f"{" ".join(line)}\n")