###############################################
### QTILE CONFIGURATION FILE OF DANIEL DIAZ ###
#
#  ____   ____
# |  _ \ |  _ \   Copyright (c) 2020 Daniel Diaz
# | | | || | | |
# | |_| || |_| |  http://www.github.com/DaniDiazTech/
# |____/ |____/
#


####### IMPORTS #########
import os
import subprocess


# from typing import List  # noqa: F401

from libqtile import hook, layout
from libqtile.config import Group, Match

# Local Files
from const import LAUNCHER
from keys.keybindings import Mouse,Keybindings

from widgets import MyWidgets
from layouts import Layouts
from groups import CreateGroups

 
###### MAIN ######
if __name__ in ["config", "__main__"]:
    # Initializes objects

    # Initializes keybindings
    obj_keys          = Keybindings()

    # Mouse
    obj_mouse         = Mouse()
    obj_widgets       = MyWidgets()
    obj_layouts       = Layouts()
    obj_groups        = CreateGroups()
    
    # Initializes qtile variables
    keys              = obj_keys.init_keys()
    mouse             = obj_mouse.init_mouse()
    layouts           = obj_layouts.init_layouts()
    groups            = obj_groups.init_groups()


    ### DISPLAYS WIDGETS IN THE SCREEN ####

    screens           = obj_widgets.init_screen()
    main_widgets_list = obj_widgets.init_widgets_list()
    widgets_screen1   = obj_widgets.init_widgets_screen()



dgroups_key_binder = None

dgroups_app_rules = []  # type: list

follow_mouse_focus = True

bring_front_click = False

cursor_warp = False


floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='dialog'),  # Dialogs stuff
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class=LAUNCHER),
])
auto_fullscreen = True

focus_on_window_activation = "smart"

reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
respect_minimize_requests = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
wmname = "BRUH"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home+'/autostart.sh'])

@hook.subscribe.client_new
def dialogs(window):
    if(window.window.get_wm_type() == 'dialog' or window.window.get_wm_transient_for()):
        window.floating = True
