import random
import classes

def main():

    with open("title_screen.txt", "r") as title:
        for line in title:
            print(line, end="")
        print()

    option = input().strip().lower()

    while option != "exit":
        if option == "start":
            start()
        elif option == "contorls":
            # show Control screen
            pass
        elif option == "exit":
            break

        option = input().strip().lower()

    
    return 1


def start():
    # Read cave from input and create a 2D map and the virtual cave.
    current_map = classes.map("TheCave.txt")
    the_cave = classes.world(current_map)

    # Place the hero and print his location (for sanity, location will go away later)
    my_hero = classes.Hero(the_cave)
    current_map.update_map(the_cave)

    print("You awake in a dark cave. You can't seem to remember how you got here, your head hurts and you can feel a pool of water beneath you.")
    action = input().strip().lower()

    while action != "exit":
        if action == "respawn":
            my_hero.spawn(the_cave)
            current_map.update_map(the_cave)

    #     if action == "look":
    #         classes.hero.look()
    #     elif action == "hear":
    #         classes.hero.hear()
    #     elif action == "attack":
    #         classes.hero.attack(action[1])
    #     elif action == "move":
    #         classes.hero.move(action[1])
    #         export_map(current_map)
        
        # current_map = update_map(current_map, the_cave)
        action = input().strip().lower()

    return


# def spwan_hero(map, the_cave):
#     # identify legal tiles
#     empty_tiles = list()
#     for row in the_cave.board:
#         for tile in row:
#             if tile.empty:
#                 empty_tiles.append(tile.coordinates)

#     # remove tiles that have a buffer
#     for row in the_cave.board:
#         for tile in row:
#             if tile.spawn_buffer > 0:
#                 for i in range(tile.spawn_buffer):
#                     for j in range(tile.spawn_buffer):
#                         if (tile.x_coordinate + i, tile.y_coordinate + j) in empty_tiles:
#                             empty_tiles.remove((tile.x_coordinate + i, tile.y_coordinate + j))
#                         if (tile.x_coordinate + i, tile.y_coordinate - j) in empty_tiles:
#                             empty_tiles.remove((tile.x_coordinate + i, tile.y_coordinate - j))
#                         if (tile.x_coordinate - i, tile.y_coordinate + j) in empty_tiles:
#                             empty_tiles.remove((tile.x_coordinate - i, tile.y_coordinate + j))
#                         if (tile.x_coordinate - i, tile.y_coordinate - j) in empty_tiles:
#                             empty_tiles.remove((tile.x_coordinate - i, tile.y_coordinate - j))

#     # # Place the hero inside the cave
#     coordinates = random.choice(empty_tiles)
#     row = 20 - coordinates[1]
#     col = coordinates[0] - 1
    
#     the_cave.board[row][col] = classes.Hero(row, col, len(the_cave.board))

#     map.update_map(the_cave)


if __name__ == '__main__':
    main()