from libqtile.config import Group

from const import GROUPS, MAGIC, V_LAST_GROUP

class CreateGroups:
    def init_groups(self):
        """
        Return the groups of Qtile
        """
        
        global V_LAST_GROUP

        V_LAST_GROUP = "1"
        return GROUPS

