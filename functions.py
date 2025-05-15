from os import name
from libqtile.layout import screensplit
from libqtile.lazy import lazy

from const import MAGIC, MAGIC_KEY, V_LAST_GROUP, nextindex, previndex, run
import groups
# from libqtile.command_client import InteractiveCommandClient


class Functions:

    ##### MOVE WINDOW IN GROUPS #####


    @staticmethod
    def magic_swap():
        @lazy.function
        def __inner(qtile):
            global V_LAST_GROUP

            win = qtile.current_window
            if not win:
                return

            __index = qtile.groups.index(qtile.current_group)
            c_group = qtile.groups[__index].name
            if c_group == MAGIC : 
                win.togroup(V_LAST_GROUP, switch_group=True)
            else : 
                win.togroup(MAGIC, switch_group=True)

        return __inner

    @staticmethod
    def window_to_prev_group():
        @lazy.function
        def __inner(qtile):
            global V_LAST_GROUP

            win = qtile.current_window
            if not win:
                return

            __index = qtile.groups.index(qtile.current_group)
            __len = len(qtile.groups)
            c_group = qtile.groups[__index].name

            if c_group == MAGIC and V_LAST_GROUP in qtile.groups_map:
                win.togroup(V_LAST_GROUP, switch_group=True)
                return

            __index = previndex(__index, __len)
            group = qtile.groups[__index].name

            if group == MAGIC:
                __index = previndex(__index, __len)
                group = qtile.groups[__index].name

            V_LAST_GROUP = group
            win.togroup(group, switch_group=True)

        return __inner

    @staticmethod
    def window_to_next_group():
        @lazy.function
        def __inner(qtile):
            global V_LAST_GROUP

            win = qtile.current_window
            if not win:
                return

            __index = qtile.groups.index(qtile.current_group)
            __len = len(qtile.groups)
            c_group = qtile.groups[__index].name

            if c_group == MAGIC and V_LAST_GROUP in qtile.groups_map:
                win.togroup(V_LAST_GROUP, switch_group=True)
                return

            __index = nextindex(__index, __len)
            group = qtile.groups[__index].name

            if group == MAGIC:
                __index = nextindex(__index, __len)
                group = qtile.groups[__index].name

            V_LAST_GROUP = group
            win.togroup(group, switch_group=True)

        return __inner

    @staticmethod
    def magic_move():
        @lazy.function
        def __inner(qtile):
            global V_LAST_GROUP

            __index = qtile.groups.index(qtile.current_group)
            c_group = qtile.groups[__index].name

            if c_group == MAGIC:
                qtile.groups_map[V_LAST_GROUP].toscreen()
            else: 
                qtile.groups_map[MAGIC].toscreen()

        return __inner

    @staticmethod
    def prev_group():
        @lazy.function
        def __inner(qtile):
            global V_LAST_GROUP

            __index = qtile.groups.index(qtile.current_group)
            __len = len(qtile.groups)
            c_group = qtile.groups[__index].name

            if c_group == MAGIC:
                if V_LAST_GROUP in qtile.groups_map:
                    qtile.groups_map[V_LAST_GROUP].toscreen()
                return

            __index = previndex(__index, __len)
            group = qtile.groups[__index].name

            if group == MAGIC:
                __index = previndex(__index, __len)
                group = qtile.groups[__index].name

            V_LAST_GROUP = group
            qtile.groups[__index].toscreen()

        return __inner

    @staticmethod
    def next_group():
        @lazy.function
        def __inner(qtile):
            global V_LAST_GROUP

            __index = qtile.groups.index(qtile.current_group)
            __len = len(qtile.groups)
            c_group = qtile.groups[__index].name

            if c_group == MAGIC:
                if V_LAST_GROUP in qtile.groups_map:
                    qtile.groups_map[V_LAST_GROUP].toscreen()
                return

            __index = nextindex(__index, __len)
            group = qtile.groups[__index].name

            if group == MAGIC:
                __index = nextindex(__index, __len)
                group = qtile.groups[__index].name

            V_LAST_GROUP = group
            qtile.groups[__index].toscreen()

        return __inner

    ##### KILL ALL WINDOWS #####
    @staticmethod
    def kill_all_windows():
        @lazy.function
        def __inner(qtile):
            for window in qtile.current_group.windows:
                window.kill()

        return __inner

    @staticmethod
    def kill_all_windows_minus_current():
        @lazy.function
        def __inner(qtile):
            for window in qtile.current_group.windows:
                if window != qtile.current_window:
                    window.kill()

        return __inner


class PWA:
    def __init__(self):
        pass
    @staticmethod
    def notion():
        return "firefox-nightly --new-window https://notion.so"
    @staticmethod
    def music():
        return "firefox-nightly --new-window https://music.youtube.com/"
    @staticmethod
    def spotify():
        return "firefox-nightly --new-window https://open.spotify.com/"
    @staticmethod
    def youtube():
        return "firefox-nightly --new-window https://www.youtube.com"
    @staticmethod
    def calendar():
        return "firefox-nightly --new-window https://calendar.google.com/calendar/"
    @staticmethod
    def habitica():
        return "firefox-nightly --new-window https://habitica.com/"

if __name__ == "__main__":
    print("This is a utilities module")
