class Spellbook:
    @staticmethod
    def validate(material, capacity):
        if not isinstance(spells, list):
            raise ValueError("Spells must be a list of spells")
        if not isinstance(material, str):
            raise ValueError("Material must be a string")
        if not isinstance(capacity, int):
            raise ValueError("Capacity must be an integer")

    def __init__(self, material, capacity, spells=[]):
        Spellbook.validate(material, capacity, spells)
        self.material = material
        self.capacity = capacity
        self.spells = spells

    def __repr__(self):
        pass

    def add_spell(self, spell):
        if not isinstance(spell, Spell):
            raise ValueError("must be an instance of the spell class")
