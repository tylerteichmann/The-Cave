# The Cave (Work in Progress)
> The Cave is a simple Python adventure game based in the command line interface (CLI).

The Cave is text-based CLI adventure game where you assume the role of the Hero who has found themselves unexpectedly in a dark cave. Navigate your way around the cave using your hearing and limited sight, but beware, rumors of a vicious monster protecting a grand treasure sourrond this cave. Will you find the treasure and escape THE CAVE!?

![](the_cave/static/title/screen.txt)

## Installation

Windows: Not yet available, but project can be compiled using pyinstaller

```sh
pyinstaller --onefile --add-data helpers.py:. main.py
```

## Usage example

Starting the application will priint a title screen to the command line that accepts the following commands:
start - Starts the game.
controls - Displays the controls for the game.

Typing _exit_ at anytime will return you to the previous screen.

When the game is started, it will prompt the user to enter a map to play on. Currently the only suppported map is TheCave.txt.

Once the map is loaded, the game will display a prompt and the user has 4 actions
move <direction> - Moves the Hero one tile in any direction. Valid inputs are cardinal directions.
hear - Displays unique text if the Hero is in listening range of the Treasure, Pit, or Monster.
look - Displays a desctription of the tiles immediately next to the Hero in each of the cardinal and subcardinal directions.
attack <direction> - The Hero attacks with a spear one tile in any direction. Will kill the Monster if in range. Valid inputs are cardinal directions.

After the Hero takes any action, the current state of the map is written to a file called _current_map.txt_ in the ./maps/ directory. This is not yet meant to be visible to the user, but may support that in future builds. Because the file is Unicode, display may varry based on application. Recommend viewing with monospace fonts.

Once the Hero makes it to the Treasure, the game is won! type exit to return to the start menu.

_For more examples and usage, please refer to the documentation._

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh

```

## Release History

* 0.0.1
    * Work in progress

## Contact Info

Tyler J. Teichmann – tyler.j.teichmann@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/tylerteichmann/)

## Contributing

1. Please send any issues and bugs to the contact information listed above.
