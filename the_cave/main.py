import sys
import os
import helpers


def main():

    start_menu()

def clear_cli():

    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

def start_menu():

    while True:
        clear_cli()

        with open("static/title_screen.txt", "r", encoding="utf-8") as screen:
            for line in screen:
                print(line, end="")
            print()

        option = input().strip().lower()

        if option == "start":
            start()
        elif option == "controls":
            control_menu()
        elif option == "exit":
            break
        else:
            continue


def control_menu():
    while True:
        clear_cli()

        with open("static/controls.txt", "r", encoding="utf-8") as screen:
            for line in screen:
                print(line, end="")
            print()

        option = input().strip().lower()

        if option == "exit":
            return
        else:
            continue


def start():
    clear_cli()
    file_name = input("Select Map: ")

    # Read cave from input and create a 2D map and the virtual cave.
    current_map = helpers.Map("maps/" + file_name)
    the_cave = helpers.World(current_map)

    # Place the hero and print his location (for sanity, location will go away later)
    my_hero = helpers.Hero(the_cave)
    current_map.update_map(the_cave)

    clear_cli()

    print("You awake in a dark cave. You can't seem to remember how you got here, your head hurts and you can feel a pool of water beneath you.")
    turn_counter = 0

    while True:
        turn_counter += 1

        action = input().strip().lower().split()

        if action == []:
            continue

        elif action[0] == "respawn":
            my_hero.spawn(the_cave)

        elif action[0] == "look":
            my_hero.look(the_cave)

        elif action[0] == "hear":
            my_hero.hear(the_cave)

        elif action[0] == "attack":
            if action[1] in my_hero.directions:
                my_hero.attack(my_hero.directions[action[1]], the_cave)
            else:
                print("Nothing happens.")

        elif action[0] == "move":
            if action[1] in my_hero.directions:
                my_hero.move(my_hero.directions[action[1]], the_cave)
            else:
                print("Nothing happens.")

        elif action[0] == "exit":
            the_cave.board[my_hero.row][my_hero.column] = helpers.Tile(my_hero.row, my_hero.column)
            current_map.update_map(the_cave)
            break
        
        else:
            print("Nothing happens.")
        
        current_map.update_map(the_cave)


if __name__ == '__main__':
    main()