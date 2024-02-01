import random

def main():
    # Generate the cave        
    the_cave = ['E'] * 20

    # Generate the exterior walls
    the_cave[0] = 'W'
    the_cave[19] = 'W'

    # obtain number of interior walls from the user
    walls = int(input("How many intererior walls in the cave (1..4)? "))
    while walls < 1 or walls > 4:
        walls = int(input("How many intererior walls in the cave (1..4)? "))

    # Create a set that contains the index of empty(legal) tiles
    empty_tiles = list()

    for i, v in enumerate(the_cave):
        if v =='E':
            empty_tiles.append(i)

    available_tiles = empty_tiles[:]

    # Generate the monster
    place(1, 'M', the_cave, available_tiles, 3)
    empty_tiles.remove(the_cave.index('M'))

    # Generate the treasure
    place(1, 'T', the_cave, available_tiles, 2)
    empty_tiles.remove(the_cave.index('T'))

    # Generate the pit
    place(1, 'P', the_cave, available_tiles, 2)
    empty_tiles.remove(the_cave.index('P'))

    # Generate the hero
    place(1, 'H', the_cave, available_tiles, 2)
    empty_tiles.remove(the_cave.index('H'))

    # Generate the interior walls
    place(walls, 'W', the_cave, empty_tiles)

    print(the_cave)


def place(quantity, object, environment, tiles, buffer=0):
    for i in range(quantity):

        location = random.choice(tiles)
        environment[location] = object

        right_buffer = location + buffer + 1
        left_buffer = location - buffer

        for i in range(left_buffer, right_buffer):
            if i in tiles:
                tiles.remove(i)


if __name__ == '__main__':
    main()