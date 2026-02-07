from random import choice, randint, random, shuffle
from enum import Enum
import pygame, pgzero, pgzrun, sys

# Check Python version number. sys.version_info gives version as a tuple, e.g. if (3,7,2,'final',0) for version 3.7.2.
# Unlike many languages, Python can compare two tuples in the same way that you can compare numbers.
if sys.version_info < (3,5):
    print("This game requires at least version 3.5 of Python. Please download it from www.python.org")
    sys.exit()

# Check Pygame Zero version. This is a bit trickier because Pygame Zero only lets us get its version number as a string.
# So we have to split the string into a list, using '.' as the character to split on. We convert each element of the
# version number into an integer - but only if the string contains numbers and nothing else, because it's possible for
# a component of the version to contain letters as well as numbers (e.g. '2.0.dev0')
# We're using a Python feature called list comprehension - this is explained in the Bubble Bobble/Cavern chapter.
pgzero_version = [int(s) if s.isnumeric() else s for s in pgzero.__version__.split('.')]
if pgzero_version < [1,2]:
    print("This game requires at least version 1.2 of Pygame Zero. You have version {0}. Please upgrade using the command 'pip3 install --upgrade pgzero'".format(pgzero.__version__))
    sys.exit()

# Set up constants
WIDTH = 800
HEIGHT = 480
TITLE = "Cavern"

NUM_ROWS = 18
NUM_COLUMNS = 28

LEVEL_X_OFFSET = 50
GRID_BLOCK_SIZE = 25

ANCHOR_CENTRE = ("center", "center")
ANCHOR_CENTRE_BOTTOM = ("center", "bottom")

LEVELS = [ ["XXXXX     XXXXXXXX     XXXXX",
            "","","","",
            "   XXXXXXX        XXXXXXX   ",
            "","","",
            "   XXXXXXXXXXXXXXXXXXXXXX   ",
            "","","",
            "XXXXXXXXX          XXXXXXXXX",
            "","",""],

           ["XXXX    XXXXXXXXXXXX    XXXX",
            "","","","",
            "    XXXXXXXXXXXXXXXXXXXX    ",
            "","","",
            "XXXXXX                XXXXXX",
            "      X              X      ",
            "       X            X       ",
            "        X          X        ",
            "         X        X         ",
            "","",""],

           ["XXXX    XXXX    XXXX    XXXX",
            "","","","",
            "  XXXXXXXX        XXXXXXXX  ",
            "","","",
            "XXXX      XXXXXXXX      XXXX",
            "","","",
            "    XXXXXX        XXXXXX    ",
            "","",""]]

def block(x,y):
    # Is there a level grid block at these coordinates?
    grid_x = (x - LEVEL_X_OFFSET) // GRID_BLOCK_SIZE
    grid_y = y // GRID_BLOCK_SIZE
    if grid_y > 0 and grid_y < NUM_ROWS:
        row = game.grid[grid_y]
        return grid_x >= 0 and grid_x < NUM_COLUMNS and len(row) > 0 and row[grid_x] != " "
    else:
        return False