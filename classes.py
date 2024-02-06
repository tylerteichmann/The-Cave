import random

class tile:
    def __init__(self, row=1, column=1, length=20):
        self.empty = True
        self.column = column
        self.x_coordinate = self.column + 1
        self.row = row
        self.y_coordinate = length - self.row
        self.coordinates = (self.x_coordinate, self.y_coordinate)
        self.spawn_buffer = 0
        self.map_symbol = 'E'

    def __str__(self):
        return f"{self.location}"

class Wall(tile):
    def __init__(self, row, column, length):
        tile.__init__(self, row, column, length)
        self.empty = False
        self.map_symbol = 'W'


class Treasure(tile):
    def __init__(self, row, column, length):
        tile.__init__(self, row, column, length)
        self.empty = False
        self.spawn_buffer = 2
        self.map_symbol = 'T'

class Pit(tile):
    def __init__(self, row, column, length):
        tile.__init__(self, row, column, length)
        self.empty = False
        self.spawn_buffer = 2
        self.map_symbol = 'P'

class Monster(tile):
    def __init__(self, row, column, length):
        tile.__init__(self, row, column, length)
        self.empty = False
        self.spawn_buffer = 3
        self.map_symbol = 'M'

class Hero(tile):
    def __init__(self, world):
        tile.__init__(self)
        self.empty = False
        self.map_symbol = 'H'
        self.spawn(world)
        self.surroundings = {
            "North":world.board[self.row + 1][self.column].map_symbol,
            "South":world.board[self.row - 1][self.column].map_symbol,
            "East":world.board[self.row][self.column + 1].map_symbol,
            "West":world.board[self.row][self.column - 1].map_symbol
        }

    def look(self, world):
        for direction in self.surroundings:
            print(f"To your {direction} you see", end='')
            if self.surroundings[direction] == 'T':
                print("the Treasure")
            elif self.surroundings[direction] == 'P':
                print("a deep pit. You try to look in but see only darkness")
            elif self.surroundings[direction] == 'M':
                print("the Monster")
            elif self.surroundings[direction] == 'W':
                print("a massive wall that seems to extend to the heavens")
            else:
                print("nothing of signifigance")           

    def hear(self):
        pass
    
    def move(self, direction):
        # if direction == "North":
        #     the_cave[self.row + 1][self.column] = Hero(self.row + 1, self.column, len(the_cave))
        pass

    def attack(self, direction):
        pass

    def spawn(self, world):
        world.board[self.row][self.column] = tile(self.row, self.column)
        
        empty_tiles = list()
        for row in world.board:
            for square in row:
                if square.empty:
                    empty_tiles.append(square.coordinates)

        # remove tiles that have a buffer
        for row in world.board:
            for square in row:
                if square.spawn_buffer > 0:
                    for i in range(square.spawn_buffer):
                        for j in range(square.spawn_buffer):
                            if (square.x_coordinate + i, square.y_coordinate + j) in empty_tiles:
                                empty_tiles.remove((square.x_coordinate + i, square.y_coordinate + j))
                            if (square.x_coordinate + i, square.y_coordinate - j) in empty_tiles:
                                empty_tiles.remove((square.x_coordinate + i, square.y_coordinate - j))
                            if (square.x_coordinate - i, square.y_coordinate + j) in empty_tiles:
                                empty_tiles.remove((square.x_coordinate - i, square.y_coordinate + j))
                            if (square.x_coordinate - i, square.y_coordinate - j) in empty_tiles:
                                empty_tiles.remove((square.x_coordinate - i, square.y_coordinate - j))

        # # Place the hero inside the cave
        coordinates = random.choice(empty_tiles)
        self.row = 20 - coordinates[1]
        self.column = coordinates[0] - 1
        
        world.board[self.row][self.column] = self
        


class map:
    def __init__(self, map_file):
        self.grid = list()
        self.import_map(map_file)

    def import_map(self, map_file):
        with open(map_file, "r") as new_map:
            for line in new_map:
                line = line.replace(" ", "")
                line = line.replace("\n", "")
                self.grid.append(list(line))

    def update_map(self, world):

        for row in world.board:
            for tile in row:
                self.grid[tile.row][tile.column] = tile.map_symbol
        
        self.export_map()

    def export_map(self):
        with open("current_map.txt", "w") as updated_map:
            for line in self.grid:
                updated_map.write(f"{" ".join(line)}\n")


class world:
    def __init__(self, map):
        self.board = list()
        self.create_world(map)

    # I think i can merge this with my __init__ unless i make it a reset function.
    def create_world(self, map):

        for r, row in enumerate(map.grid):
            new_row = list()

            for c, square in enumerate(row):
                if square == 'E':
                    new_row.append(tile(r, c, len(row)))
                elif square == 'W':
                    new_row.append(Wall(r, c, len(row)))
                elif square == 'P':
                    new_row.append(Pit(r, c, len(row)))
                elif square == 'T':             
                    new_row.append(Treasure(r, c, len(row)))
                elif square == 'M':
                    new_row.append(Monster(r, c, len(row)))
            
            self.board.append(new_row)

        map.update_map(self)