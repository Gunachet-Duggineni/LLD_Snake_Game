# This file stores all the settings that make the Pacman game work, like colors, sizes, and speeds.
# constants.py is used for:
#   Storing settings like Pacman’s color, ghost speeds, and screen size.
#   Keeping all fixed values in one place, making it easy to adjust the game.
#   Ensuring that everything looks and feels consistent across the game.

# constants.py is used in:
#   sprites.py, pacman.py, ghosts.py, and entity.py to provide values for colors, sizes, and speeds.

# In short: constants.py is like the game’s setup guide, keeping settings organized and easy to adjust!


# Any modifications to game layout, structure, or gameplay mechanics (e.g., changing tile size or adding new game states) should be made in constants.py to ensure consistency across the game project


TILEWIDTH = 16
TILEHEIGHT = 16
NROWS = 36
NCOLS = 28
SCREENWIDTH = NCOLS*TILEWIDTH
SCREENHEIGHT = NROWS*TILEHEIGHT
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255,100,150)
TEAL = (100,255,255)
ORANGE = (230,190,40)
GREEN = (0, 255, 0)

STOP = 0
UP = 1
DOWN = -1
LEFT = 2
RIGHT = -2

PACMAN = 0 #represents player or main character
PORTAL = 3 #to know where portals are so that when character touches it, something special happens
PELLET = 1 #represents the items character eats to score points. everytime it eats a pellet it inc
POWERPELLET = 2
GHOST = 3

SCATTER = 0
CHASE = 1
FREIGHT = 2
SPAWN = 3
BLINKY = 4
PINKY = 5
INKY = 6
CLYDE = 7
FRUIT = 8

SCORETXT = 0
LEVELTXT = 1
READYTXT = 2
PAUSETXT = 3
GAMEOVERTXT = 4