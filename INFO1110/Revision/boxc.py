class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        weight = int()

class Box:
    def __init(self, items, total_weight):
        self.items = items
        items = []
        self.weight = total_weight
        total_weight = 0

    def add_item(self, name, weight):
        Item.name = name
        Item.weight = weight
        self.items.append(name)
        self.total_weight += weight

    def get_weight(self):
        return self.total_weight

b = Box()
b.add_item(Item('Cat', 5))
b.add_item(Item('Nintendo Switch', 1))
b.add_item(Item('Potatoes', 2))

msg = 'The box weighs {} kg'.format(b.get_weight())
print(msg)
