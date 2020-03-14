class Item:
    def __init__(self, name, short, skill_bonus, will_bonus):
        self.name = name
        self.short = short
        self.skill_bonus = skill_bonus
        self.will_bonus = will_bonus
        """TODO: Initialises an item."""


    def get_name(self):
        return self.name
        """TODO: Returns an item's name."""


    def get_short(self):
        return self.short
        """TODO: Returns an item's short name."""


    def get_info(self):
        return("Name: {}, Short: {}, Skill bonus: {:.d}, Will bonus: {:.d}").format(self.name, self.short, self.skill_bonus, self.will_bonus)
        """TODO: Prints information about the item."""


    def get_skill(self):
        return self.skill_bonus
        """TODO: Returns the item's skill bonus."""


    def get_will(self):
        return self.will_bonus
        """TODO: Returns the item's will bonus."""
		
