
from os import path
from libqtile.confreader import ConfigError

# Import default mod keys
from keys.default import *

from functions import PWA

from os.path import expanduser

from const import *


# ------------ Hardware Configs ------------
HARDWARE_KEYS = [
    # (Modifier, Key, Command)

    # Volume
    ([], "XF86AudioLowerVolume", "pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ([], "XF86AudioRaiseVolume", "pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ([], "XF86AudioMute", "pactl set-sink-mute @DEFAULT_SINK@ toggle"),
     
    # Brightness
    ([], "XF86MonBrightnessUp", "brightnessctl set +5%"),
    ([], "XF86MonBrightnessDown", "brightnessctl set 5%-"),
]


APPS = [
    ([MOD], "t", TERMINAL),
    # (Modifier, Key, Command)
    ([MOD],      "e", FILE_EXPLORER),
    ([MOD], "f", BROWSER),
    ([MOD], "c", "code"),
    ([MOD, ALT], "p", "pycharm"),
    ([MOD, ALT], "a", "pavucontrol"),
    ([MOD, ALT], "e", "vim -g .config/qtile/config.py"),

    # Media hotkeys
    ([MOD],      "Up", "pulseaudio-ctl up 5"),
    ([MOD],      "Down", "pulseaudio-ctl down 5"),
    
    # Makes reference to play-pause script
    # You can find it in my scripts repository
    ([ALTGR],    "space", " playerctl play-pause"),
   
    # Run "rofi-theme-selector" in terminal to select a theme
    ([MOD], "space", run("rofi.sh")),
    ([MOD], "w", run("wallselect.sh")),

    # Terminal apps
    ([MOD, ALT], "n", TERMINAL + " -e nvim"),

    
    ([MOD], "p", "flameshot gui"),
    ([MOD], "v", "clipcat-menu --rofi-menu-length 10"),
]

##########################
# Your custom keys here  #
##########################

CUSTOM_SPAWN_KEYS = [
    # PWA keys
    ([MOD, ALT], "s", PWA.spotify()),
    ([MOD, ALT], "m", PWA.music()),
    ([MOD, ALT], "t", PWA.calendar()),
    ([MOD, ALT], "y", PWA.youtube()),
    ([MOD, ALT], "l", PWA.notion()),
    ([MOD, ALT], "h", PWA.habitica()),
]


SPAWN_KEYS = HARDWARE_KEYS + APPS + CUSTOM_SPAWN_KEYS 

SPAWN_CMD_KEYS = [
    # Takes full screenshot and creates a file on the screenshot folder
]
