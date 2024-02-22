import random
import classes

def main():
    while True:

        with open("title_screen.txt", "r") as title:
            for line in title:
                print(line, end="")
            print()

        option = input().strip().lower()

        if option == "start":
            start()

        elif option == "controls":

            with open("controls.txt", "r") as title:
                for line in title:
                    print(line, end="")
                print()

            option = input().strip().lower()

        elif option == "exit":
            break

    return 0


def start():
    # Read cave from input and create a 2D map and the virtual cave.
    current_map = classes.map("TheCave.txt")
    the_cave = classes.world(current_map)

    # Place the hero and print his location (for sanity, location will go away later)
    my_hero = classes.Hero(the_cave)
    current_map.update_map(the_cave)

    print("You awake in a dark cave. You can't seem to remember how you got here, your head hurts and you can feel a pool of water beneath you.")

    while True:

        action = input().strip().lower().split()
        if action == []:
            continue

        if action[0] == "respawn":
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
            the_cave.board[my_hero.row][my_hero.column] = classes.tile(my_hero.row, my_hero.column)
            current_map.update_map(the_cave)
            break
        
        else:
            print("Nohting happens.")
        
        current_map.update_map(the_cave)

    return 0


if __name__ == '__main__':
    main()