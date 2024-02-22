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
        # I think i can use class instead of the symbol
        self.map_symbol = ' '

    def kill(self, world):
        world.board[self.row][self.column] = tile(self.row, self.column)
       

    def __str__(self):
        return f"{self.location}"


class Wall(tile):
    map_symbol = '\u25A0'

    def __init__(self, row, column, length):
        tile.__init__(self, row, column, length)
        self.empty = False
        self.map_symbol = Wall.map_symbol


class Treasure(tile):
    map_symbol = 'T'

    def __init__(self, row, column, length):
        tile.__init__(self, row, column, length)
        self.empty = False
        self.spawn_buffer = 2
        self.map_symbol = Treasure.map_symbol


class Pit(tile):
    map_symbol = '\u25CB'

    def __init__(self, row, column, length):
        tile.__init__(self, row, column, length)
        self.empty = False
        self.spawn_buffer = 2
        self.map_symbol = Pit.map_symbol


class Monster(tile):
    map_symbol = '\u25C6'

    def __init__(self, row, column, length):
        tile.__init__(self, row, column, length)
        self.empty = False
        self.spawn_buffer = 3
        self.map_symbol = Monster.map_symbol


class Hero(tile):
    map_symbol = 'H'

    def __init__(self, world):
        tile.__init__(self)
        self.empty = False
        self.map_symbol = Hero.map_symbol
        self.hearing_range = 2
        self.sight = 1
        self.attack_range = 2
        self.movement = 1
        self.directions = {
            "north":(-1, 0),
            "northeast":(-1, +1),
            "east":(0, +1),
            "southeast":(+1, +1),
            "south":(+1, 0),
            "southwest":(+1, -1),
            "west":(0, -1),
            "northwest":(-1, -1)
        }
        self.spawn(world)


    def look(self, world):
        print(f"To your shine your flashlight")
        for y in range(-self.sight, self.sight + 1):
            for x in range(-self.sight, self.sight + 1):
                if (x, y) == (0, 0):
                    continue

                symbol = world.board[self.row + y][self.column + x].map_symbol

                for key in self.directions:
                    if self.directions[key] == (y, x):
                        direction = key

                if symbol == Treasure.map_symbol:
                    print(f"To the {direction} you see the Treasure.")
                elif symbol == Pit.map_symbol:
                    print(f"To the {direction} you see a deep pit. You try to look in but see only darkness")
                elif symbol == Monster.map_symbol:
                    print(f"To the {direction} you see the Monster")
                elif symbol == Wall.map_symbol:
                    print(f"To the {direction} you see a massive wall that seems to extend to the heavens")
                else:
                    print(f"To the {direction} you see nothing of signifigance")
   

    def hear(self, world):
        nothing = True
        for y in range(-self.hearing_range, self.hearing_range + 1):
            for x in range(-self.hearing_range, self.hearing_range + 1):
                symbol = world.board[self.row + y][self.column + x].map_symbol
                if symbol == Treasure.map_symbol:
                    print(f"You can hear a clinking of coins, a great treasure is nearby.")
                    nothing = False
                elif symbol == Pit.map_symbol:
                    print(f"You can hear a faint wind, perhapse indicateing some deep void.")
                    nothing = False
                elif symbol == Monster.map_symbol:
                    print(f"You hear a Snarling noise, but can't tell where its coming from...")
                    nothing = False
        if nothing:
            print(f"You can't seem to hear anything") 
    

    def move(self, direction, world):
        # # check if moving to a valid tile
        symbol = world.board[self.row + direction[0]][self.column + direction[1]].map_symbol
        if symbol !=  Wall.map_symbol:
            if symbol == 'T':
                print(f"You Win!")
            elif symbol == 'P' or symbol == 'M':
                print(f"Game Over...")
            else:
                # replace the old pointer with "E"
                world.board[self.row][self.column] = tile(self.row, self.column)
                # Update hero's location
                self.row += direction[0]
                self.column += direction[1]
                # change the world pointer location
                world.board[self.row][self.column] = self
        else:
            print(f"The way is blocked...")


    def attack(self, direction, world):
        if world.board[self.row + direction[0]][self.column + direction[1]].map_symbol == Monster.map_symbol:
            # Kill Monster Function
            print("The monster has been slain")
            world.board[self.row + direction[0]][self.column + direction[1]].kill(world)
        else:
            print("Your spear falls to the ground, forever lost in the darkness...")

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

        # Place the hero inside the cave
        coordinates = random.choice(empty_tiles)
        self.row = 20 - coordinates[1]
        self.column = coordinates[0] - 1
        
        # Update the world with the hero
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
        with open("current_map.txt", "w", encoding="UTF-8") as updated_map:
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