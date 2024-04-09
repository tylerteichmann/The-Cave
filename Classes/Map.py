class Map:

    def __init__(self, map_file):
        self.grid = list()
        self.import_map(map_file)

    def import_map(self, map_file):
        with open(map_file, "r") as new_map:
            for line in new_map:
                line = line.replace(" ", "")
                line = line.replace("\n", "")
                self.grid.append(list(line))

    def update_map(self, World):

        for row in World.board:
            for Tile in row:
                self.grid[Tile.row][Tile.column] = Tile.map_symbol
        
        self.export_map()

    def export_map(self):
        with open("current_Map.txt", "w", encoding="UTF-8") as updated_map:
            for line in self.grid:
                updated_map.write(f"{" ".join(line)}\n")