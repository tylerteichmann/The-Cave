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

    # Generate the monster
    place('M', 1, the_cave)

    # Generate the treasure
    place('T', 1, the_cave)

    # Generate the pit
    place('P', 1, the_cave)

    # Generate the hero
    place('H', 1, the_cave)

    # Generate the interior walls
    place('W', walls, the_cave)


    print(the_cave)


def place(object, quantity, enviornment):
    for i in range(quantity):
        #Choose a reandom location
        location = random.randrange(len(enviornment))

        while enviornment[location] != 'E':
            if object != 'W':
                for i in range(3):
                    if enviornment[location + i] != 'E' or enviornment[location - i] != 'E':
                        break
                if enviornment[location + i] != 'E' or enviornment[location - i] != 'E':

            location = random.randrange(len(enviornment))
                    
        enviornment[location] = object


if __name__ == '__main__':
    main()