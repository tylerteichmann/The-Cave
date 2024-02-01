import random

def main():
       
    # Read cave from input and create a 2D array.'
    the_cave = import_map()

    # Place the hero
    coordinates = place_hero(the_cave)

    # # Print hero's location
    print(coordinates)

    # # Write the new cave to a new file
    export_map(the_cave)

    return


def import_map():
    the_cave = list()
    
    with open("TheCave.txt", "r") as map:
        for line in map:
            line = line.replace(" ", "")
            line = line.replace("\n", "")
            the_cave.append(list(line))

    return the_cave

def place_hero(the_cave):
    # identify legal tiles
    empty_tiles = list()
    for x, row in enumerate(the_cave):
        for y, tile in enumerate(row):
            if tile == 'E':
                empty_tiles.append((x, y))

    # # Place the hero inside the cave
    for i in range(1):
        location = random.choice(empty_tiles)
        the_cave[location[1]][location[0]] = 'H'
    
    coordinates = location[0] + 1, len(the_cave) - location[1]

    return coordinates


def export_map(the_cave):
    with open("TheCaveUpdated.txt", "w") as updated_map:
        for line in the_cave:
            for tile in line:
                updated_map.write(str(tile) + " ")
            updated_map.write("\n")


if __name__ == '__main__':
    main()