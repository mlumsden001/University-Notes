class Box:
    def __init__ (self, name, total_weight, item):
        self.item = item
        self.total_weight = total_weight

    def add_item(self, item):
        self.item = item

    def get_total_weight(self, total_weight):
        return self.total_weight

class Item:
    def __init__(self, weight, name):
        self.weight = weight
        self.name = name
