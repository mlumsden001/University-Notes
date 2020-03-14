class Room:
    @staticmethod
    def validate(name):
        if not isinstance(name, str):
            return ValueError("The room name must be a string")
        if not isinstance(desc, str):
            return ValueError("Description must be a string")
        if not isinstance(quest, str):
            return ValueError("Quest must be a string")
        if not isinstance)action, str):
            return ValueError("Action must be a string")
        if not isinstance(path, str):
            return ValueError("Path must be a string")
        if not isinstance(dir, str):
            return ValueError("Direction must be a string")
        if not isinstance(dest, str):
            return ValueError("Destination must be a string")

    def __init__(self, name, desc, quest, action, path, dir):
		self.name = name
        self.desc = desc
        self.quest = quest
        self.action = action
        self.path = path
        self.dir = dir
        self.dest = dest

	def get_name(self):
        return self.name
        """TODO: Returns the room's name."""
		...

	def get_short_desc(self):
        return self.desc
        """TODO: Returns a string containing a short description of the room. This description changes based on whether or not a relevant quest has been completed in this room.

		If there are no quests that are relevant to this room, this should return: 'There is nothing in this room.' """
		...

	def get_quest_action(self):
        return self.action
        """TODO: If a quest can be completed in this room, returns a command that the user can input to attempt the quest."""
		...

	def set_quest(self, q):

        """TODO: Sets a new quest for this room."""
		...

	def get_quest(self):
        return self.quest
        """TODO: Returns a Quest object that can be completed in this room."""
		...

	def set_path(self, dir, dest):
		"""TODO: Creates an path leading from this room to another."""
		...

	def draw(self):
		"""TODO: Creates a drawing depicting the exits in each room."""
		print('+--------------------+')
        print('|                    |')
        print('|                    |')
        print('|                    |')
        print('|                    |')
        print('|                    |')
        print('|                    |')
        print('|                    |')
        print('|                    |')
        print('|                    |')
        print('+--------------------+')'

	def move(self, dir):
        if dir == "NORTH":
            return self.quest
        """TODO: Returns an adjoining Room object based on a direction given. (i.e. if dir == "NORTH", returns a Room object in the north)."""
		...
