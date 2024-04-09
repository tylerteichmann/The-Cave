from classes.tile import Tile
from classes.wall import Wall
from classes.pit import Pit
from classes.treasure import Treasure
from classes.monster import Monster

class World:
    def __init__(self, Map):
        self.board = list()
        self.create_world(Map)

    # I think i can merge this with my __init__ unless i make it a reset function.
    def create_world(self, Map):

        for r, row in enumerate(Map.grid):
            new_row = list()

            for c, square in enumerate(row):
                if square == 'E':
                    new_row.append(Tile(r, c, len(row)))
                elif square == 'W':
                    new_row.append(Wall(r, c, len(row)))
                elif square == 'P':
                    new_row.append(Pit(r, c, len(row)))
                elif square == 'T':             
                    new_row.append(Treasure(r, c, len(row)))
                elif square == 'M':
                    new_row.append(Monster(r, c, len(row)))

            self.board.append(new_row)

        Map.update_map(self)