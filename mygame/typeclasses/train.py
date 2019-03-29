# file mygame/typeclasses/train.py

from evennia import DefaultObject
from evennia import DefaultObject
from commands.train import CmdSetTrain


class TrainObject(DefaultObject):

    def at_object_creation(self):
        self.cmdset.add_default(CmdSetTrain)
