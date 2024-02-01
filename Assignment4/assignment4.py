import random
import classes

def main():

    with open("title_screen.txt", "r") as title:
        for line in title:
            print(line, end="")
        print()

    option = input()

    while option != "exit":
        if option == "start":
            option = start()
            continue
        elif option == "contorls":
            # show Control screen
            pass
        elif option == "exit":
            break

        option = input()

    
    return 1


def start():
    #add a map class with import() update() export()

    # Read cave from input and create a 2D array.
    current_map = import_map()

    # Create the cave from the map.
    the_cave = create_cave(current_map)

    # Place the hero
    coordinates = place_hero(current_map, the_cave)

    # Print hero's location
    print(coordinates)

    # current_map = update_map(current_map, the_cave)

    export_map(current_map)

    print("You awake in a dark cave. You can't seem to remember how you got here, your head hurts and you can feel a pool of water beneath you.")
    action = input()

    while action != "exit":
        
    #     if action == "look":
    #         classes.hero.look()
    #     elif action == "hear":
    #         classes.hero.hear()
    #     elif action == "attack":
    #         classes.hero.attack(action[1])
    #     elif action == "move":
    #         classes.hero.move(action[1])
    #         export_map(current_map)
        
        action = input()


    # Write the new cave to a new file
    export_map(current_map)

    # for row in the_cave:
    #     print(row)


    return action


def import_map():
    map = list()
    
    with open("TheCave.txt", "r") as map_file:
        for line in map_file:
            line = line.replace(" ", "")
            line = line.replace("\n", "")
            map.append(list(line))

    return map


def create_cave(map):

    the_cave = list()

    for r, row in enumerate(map):
        new_row = list()

        for c, tile in enumerate(row):
            if tile == 'E':
                new_row.append(classes.tile(r, c, len(row)))
            elif tile == 'W':
                new_row.append(classes.Wall(r, c, len(row)))
            elif tile == 'P':
                new_row.append(classes.Pit(r, c, len(row)))
            elif tile == 'T':             
                new_row.append(classes.Treasure(r, c, len(row)))
        
        the_cave.append(new_row)

    return the_cave

# def update_map(map, the_cave):
#     for row in the_cave:
#         for tile in row:



def place_hero(map, the_cave):
    # identify legal tiles
    empty_tiles = list()

    for row in the_cave:
        for tile in row:
            if tile.empty:
                empty_tiles.append(tile.coordinates)
    # remove tiles that have a buffer
    for row in the_cave:
        for tile in row:
            if tile.spawn_buffer > 0:
                for i in range(tile.spawn_buffer):
                    for j in range(tile.spawn_buffer):
                        if (tile.x_coordinate + i, tile.y_coordinate + j) in empty_tiles:
                            empty_tiles.remove((tile.x_coordinate + i, tile.y_coordinate + j))
                        if (tile.x_coordinate + i, tile.y_coordinate - j) in empty_tiles:
                            empty_tiles.remove((tile.x_coordinate + i, tile.y_coordinate - j))
                        if (tile.x_coordinate - i, tile.y_coordinate + j) in empty_tiles:
                            empty_tiles.remove((tile.x_coordinate - i, tile.y_coordinate + j))
                        if (tile.x_coordinate - i, tile.y_coordinate - j) in empty_tiles:
                            empty_tiles.remove((tile.x_coordinate - i, tile.y_coordinate - j))

    # # Place the hero inside the cave
    coordinates = random.choice(empty_tiles)
    row = 20 - coordinates[1]
    col = coordinates[0] - 1    
    the_cave[row][col] = classes.Hero(row, col, len(the_cave))
    map[row][col] = 'H'

    return the_cave[row][col].coordinates


def export_map(the_cave):
    with open("TheCaveUpdated.txt", "w") as updated_map:
        for line in the_cave:
            updated_map.write(f"{" ".join(line)}\n")
    
    return


if __name__ == '__main__':
    main()