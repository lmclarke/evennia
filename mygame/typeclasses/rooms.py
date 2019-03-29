"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
from evennia.contrib.rpsystem import ContribRPRoom
from collections import defaultdict
from evennia.utils import list_to_string

ROOM_NAME_COL = "|C"
INDENT = "   "


class Room(ContribRPRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """

    def return_appearance_header(self, looker, **kwargs):
        color = self.db.color
        display_name = self.get_display_name(looker)
        if color:
            display_name = '|%s%s|n' % display_name
        return ROOM_NAME_COL + display_name + "|W"

    def return_appearance_body(self, looker, **kwargs):
        return INDENT + self.db.desc if self.db.desc else ''

    def return_appearance_contents(self, looker, **kwargs):
        thing_strings = []
        for key, itemlist in sorted(kwargs['things'].items()):
            nitem = len(itemlist)
            if nitem == 1:
                key, _ = itemlist[0].get_numbered_name(nitem, looker, key=key)
            else:
                key = [item.get_numbered_name(nitem, looker, key=key)[1] for item in itemlist][0]
            thing_strings.append(key)

        return "\n".join(kwargs['users'] + thing_strings)

    def return_appearance_exits(self, looker, **kwargs):
        return "\n|C[|W Exits:|n " + list_to_string(kwargs['exits']) + "|C]|W"

    def return_appearance(self, looker, **kwargs):
        """
        This formats a description. It is the hook a 'look' command
        should call.

        Args:
            looker (Object): Object doing the looking.
            **kwargs (dict): Arbitrary, optional arguments for users
                overriding the call (unused by default).
        """
        if not looker:
            return ""
        # get and identify all objects
        visible = (con for con in self.contents if con != looker and
                   con.access(looker, "view"))
        exits, users, things = [], [], defaultdict(list)
        for con in visible:
            key = con.get_display_name(looker)
            if con.destination:
                exits.append(key)
            elif con.has_account:
                users.append("|c%s |n" % key + con.db.pose if con.db.pose else '')
            else:
                # things can be pluralized
                things[key].append(con)

        # get description, build string
        string = self.return_appearance_header(looker, **kwargs)
        string += "\n" + self.return_appearance_body(looker, **kwargs)
        if exits:
            string += '\n' + self.return_appearance_exits(looker, exits=exits, **kwargs)
        if users or things:
            string += '\n' + self.return_appearance_contents(looker, users=users, things=things, **kwargs)

        return string
