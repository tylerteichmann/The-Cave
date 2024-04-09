import random

from classes.tile import Tile
from classes.wall import Wall
from classes.pit import Pit
from classes.treasure import Treasure
from classes.monster import Monster

class Hero(Tile):
    map_symbol = 'H'

    def __init__(self, World):
        Tile.__init__(self)
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
        self.spawn(World)


    def look(self, World):
        print(f"To your shine your flashlight")
        for y in range(-self.sight, self.sight + 1):
            for x in range(-self.sight, self.sight + 1):
                if (x, y) == (0, 0):
                    continue

                symbol = World.board[self.row + y][self.column + x].map_symbol

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
   

    def hear(self, World):
        nothing = True
        for y in range(-self.hearing_range, self.hearing_range + 1):
            for x in range(-self.hearing_range, self.hearing_range + 1):
                symbol = World.board[self.row + y][self.column + x].map_symbol
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
    

    def move(self, direction, World):
        # # check if moving to a valid Tile
        symbol = World.board[self.row + direction[0]][self.column + direction[1]].map_symbol
        if symbol !=  Wall.map_symbol:
            if symbol == 'T':
                print(f"You Win!")
            elif symbol == 'P' or symbol == 'M':
                print(f"Game Over...")
            else:
                # replace the old pointer with "E"
                World.board[self.row][self.column] = Tile(self.row, self.column)
                # Update hero's location
                self.row += direction[0]
                self.column += direction[1]
                # change the World pointer location
                World.board[self.row][self.column] = self
        else:
            print(f"The way is blocked...")


    def attack(self, direction, World):
        if World.board[self.row + direction[0]][self.column + direction[1]].map_symbol == Monster.map_symbol:
            # Kill Monster Function
            print("The monster has been slain")
            World.board[self.row + direction[0]][self.column + direction[1]].kill(World)
        else:
            print("Your spear falls to the ground, forever lost in the darkness...")

    def spawn(self, World):
        World.board[self.row][self.column] = Tile(self.row, self.column)
        
        empty_Tiles = list()
        for row in World.board:
            for square in row:
                if square.empty:
                    empty_Tiles.append(square.coordinates)

        # remove Tiles that have a buffer
        for row in World.board:
            for square in row:
                if square.spawn_buffer > 0:
                    for i in range(square.spawn_buffer):
                        for j in range(square.spawn_buffer):
                            if (square.x_coordinate + i, square.y_coordinate + j) in empty_Tiles:
                                empty_Tiles.remove((square.x_coordinate + i, square.y_coordinate + j))
                            if (square.x_coordinate + i, square.y_coordinate - j) in empty_Tiles:
                                empty_Tiles.remove((square.x_coordinate + i, square.y_coordinate - j))
                            if (square.x_coordinate - i, square.y_coordinate + j) in empty_Tiles:
                                empty_Tiles.remove((square.x_coordinate - i, square.y_coordinate + j))
                            if (square.x_coordinate - i, square.y_coordinate - j) in empty_Tiles:
                                empty_Tiles.remove((square.x_coordinate - i, square.y_coordinate - j))

        # Place the hero inside the cave
        coordinates = random.choice(empty_Tiles)
        self.row = 20 - coordinates[1]
        self.column = coordinates[0] - 1
        
        # Update the World with the hero
        World.board[self.row][self.column] = self