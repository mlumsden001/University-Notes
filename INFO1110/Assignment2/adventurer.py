class Adventurer:
    @staticmethod
    def validate(inventory, skill, will):
        if not isinstance(inventory, list):
            return ValueError("Inventory must be a list")
        if not isinstance(skill, int):
            return ValueError("Skill must be an integer")
        if not isinstance(will, int):
            return ValueError("Will must be an integer")

    def __init__(self, inventory, skill, will):
        self.invetory = inventory
        inventory = []
        self.skill = skill
        self.will = will
        self.skill = 5
        self.will = 5
        Adventurer.validate(inventory, skill, will)
    def get_inv(self):
        return self.inventory


    def get_skill(self):
        return self.skill
        """TODO: Returns the adventurer's skill level. Whether this value is generated before or after item bonuses are applied is your decision to make."""


    def get_will(self):
        """TODO: Returns the adventurer's will power. Whether this value is generated before or after item bonuses are applied is your decision to make."""
        return self.will

    def take(self, item):
        i += 1
        inventory.append(self.item)
        """TODO: Adds an item to the adventurer's inventory."""

    def check_self(self):
        return "Inventory: ", inventory, ". Will: {}. Skill: {}".format(self.will, self.skill)
        """TODO: Shows adventurer stats and all item stats."""
