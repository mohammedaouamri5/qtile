

from os import path
from os.path import expanduser

from libqtile.config import Group
"""Qtile default keybindings"""

# Keys
MOD = "mod4"
ALT = "mod1"
ALTGR = "mod5"
SHIFT = "shift"
CONTROL = "control"

# Basic wm bindings

# All of these variables include the MOVEMENT_KEYS at the start

# The key which the WM will use to move the layouts
MOVEMENT_KEY   = MOD
KILL_KEY       = MOD

SWAP_KEY       = SHIFT
FLOATING_KEY   = SHIFT


############   BINDINGS FOR MONADTALL   ##############
# Move between windows
LEFT   = "h"
RIGHT  = "l"
DOWN   = "j"
UP     = "k"

# Swap windows 
SWAP_LEFT  = "h"
SWAP_RIGHT = "l"
SWAP_DOWN  = "j"
SWAP_UP    = "k"

SWAP_FLIP  = "space" # Flip the layout

###########         LAYOUTS               ###############
# Change windows lenght
GROW       = "i"
SHRINK     = "m"
NORMALIZE  = "n"
MAXIMIZE   = "o"

# Floating layout
TOOGLE_FLOATING = "w"
TOOGLE_FULL     = "g"

# Groups key
# Move screen to next and previous group
NEXT     = "k"
PREVIOUS = "j"

# Kill Functions
KILL_CURRENT           = "q"
KILL_ALL               = "x"
KILL_ALL_MINUS_CURRENT = "c"

# Rotates layouts

TOOGLE_LAYOUT = "Tab"



HOME = expanduser("~")

# Define constants here
TERMINAL = "konsole"
FILE_EXPLORER = "dolphin"
BROWSER = "firefox-nightly"

SCRIPTS_DIR = path.join(HOME , ".scripts") 
    

# Basic window manager movements


# Qtile shutdown/restart keys
SHUTDOWN_MODIFIER = [MOD, CONTROL]
RESTART           = "r"
SHUTDOWN          = "q"


# Group movement keys:
GROUPS_KEY     = SHIFT
SWAP_GROUP_KEY = CONTROL

NEXT_GROUP = "k"
PREV_GROUP = "j"

MAGIC = 'MAGIC'
MAGIC_KEY = 's'

GROUPS = [
            Group("1", label="一", layout="monadtall"),
            Group("2", label="二", layout="monadtall"),
            Group("3", label="三", layout="monadtall"),
            Group("4", label="四", layout="monadtall"),
            Group("5", label="五", layout="monadtall"),
            Group("6", label="六", layout="monadtall"),
            Group("7", label="七", layout="monadtall"),
            Group("8", label="八", layout="monadtall"),
            Group("9", label="九", layout="monadtall"),
            Group("10", label="十", layout="monadtall"),
            Group("100", label="百", layout="monadtall"),
            Group("1000", label="千", layout="monadtall"),
            Group("10000", label="万", layout="monadtall"),
            Group(name=MAGIC, label="", layout="monadtall"),
        ]



# FUNCTIONS 

def run(__script) : 
    return path.join(SCRIPTS_DIR  , __script) 

def nextindex(__index,__len): 
    return  ( __index + 1 ) % __len

def previndex(__index,__len): 
    return  ( __index - 1 ) % __len
# VARIABLE
V_LAST_GROUP = GROUPS[0].name
