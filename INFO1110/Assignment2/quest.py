from adventurer import Adventurer

class Quest:
    def __init__(self, reward, action, desc, before, after, req, fail_msg, pass_msg, room):
        self.reward = reward
        self.action = action
        self.desc = desc
        self.before = before
        self.after = after
        self.req = req
        self.fail_msg = fail_msg
        self.pass_msg = pass_msg
        self.room = room
        """TODO: Initialises a quest."""


    def get_info(self):
        return self.desc
        """TODO: Returns the quest's description."""


    def is_complete(self):
        complete_quests = []
        if self.pass_msg == True:
            complete_quests.append(Room(quest))
            return self.pass_msg
        else:
            return self.fail_msg
        """TODO: Returns whether or not the quest is complete."""


    def get_action(self):
        return self.action
        """TODO: Returns a command that the user can input to attempt the quest."""


    def get_room_desc(self):
        if is_complete(self.quest) == True:
            return self.after
        else:
            return self.before
        """TODO: Returns a description for the room that the quest is currently in. Note that this is different depending on whether or not the quest has been completed."""


    def attempt(self, player):
        if Adventurer(will) > self.req:
            Adventurer(will).is_complete == True
        else:
            Adventurer(will).is_complete == False
        """TODO: Allows the player to attempt this quest.

		Check the cumulative skill or will power of the player and all their items. If this value is larger than the required skill or will threshold for this quest's completion, they succeed and are rewarded with an item (the room's description will also change because of this).

		Otherwise, nothing happens."""
