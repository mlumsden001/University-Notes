from room import Room
from item import Item
from adventurer import Adventurer
from quest import Quest
import sys

if len(sys.argv) < 4:
    print("Usage: python3 simulation.py <items> <paths> <quests>")
    sys.exit(1)

try:
    path_config = open(sys.argv[1], 'r')
    item_config = open(sys.argv[2], 'r')
    quest_config = open(sys.argv[3], 'r')




def read_paths(source):
    p = open(source, 'r')
    paths = []
    line = p.readline()
    while True:
        paths.append(line)
        if line == '':
            break

    p.close()
    return paths
    #"""Returns a list of lists according to the specifications in a config file, (source).

	#source contains path specifications of the form:
	#origin > direction > destination.

	#read_paths() interprets each line as a list with three elements, containing exactly those attributes. Each list is then added to a larger list, `paths`, which is returned."""


def create_rooms(paths):
    count = 0
    rooms = []
    while count < len(paths):
        if paths[count] == 'Entrance > NORTH > Foyer':
            rooms.append('Foyer')
        if paths[count] == 'Foyer > NORTH > Courtyard':
            rooms.append('Courtyard')
        if paths[count] == 'Foyer > EAST > Parlour':
            rooms.append('Parlour')
        if paths[count] == 'Foyer > SOUTH > Entrance':
            rooms.append('Entrance')
        if paths[count] == 'Foyer > WEST > Workshop':
            rooms.append('Workshop')
        if paths[count] == 'Courtyard > SOUTH > Foyer':
            rooms.append('Foyer')
        if paths[count] == 'Parlour > WEST > Foyer':
            rooms.append('Foyer')
        if paths[count] == 'Workshop > EAST > Foyer':
            rooms.append('Foyer')
        else:
            pass
        count += 1
    return rooms

    """Receives a list of paths and returns a list of rooms based on those paths. Each room will be generated in the order that they are found."""


def generate_items(source):
	#"""Returns a list of items according to the specifications in a config file, (source).

	#source contains item specifications of the form:
	#item name | shortname | skill bonus | will bonus
	#"""

    items = []
    i = open(source, 'r')
    line = i.readline()
    while True:
        if line == '':
            break
        item.append(line)
    i.close()
    return items

def generate_quests(source, items, rooms):
	#"""Returns a list of quests according to the specifications in a config file, (source).

	#source contains quest specifications of the form:
	#reward | action | quest description | before_text | after_text | quest requirements | failure message | success message | quest location
	#"""
    quests = []
    q = open(source, 'r')
    line = q.readline()
    while True:
        while line != '':
            quests.append(line)
        if line == '':
            break
    q.close()
    return quests


# TODO: Retrieve info from CONFIG files. Use this information to make Adventurer, Item, Quest, and Room objects.
paths_list = read_paths(sys.argv[2])
room_list = create_rooms(paths_list)
item_list = generate_items(sys.argv[3])
quest_list = generate_quests(sys.argv[4], item_list, room_list)

# TODO: Receive commands from standard input and act appropriately.
while True:
    user_input = str(input('>>> '))
    if user_input == 'QUIT':
        print("Bye!")
        break
    elif user_input == 'HELP':
        print('HELP       - Shows some availabek commands.')
        print('LOOK or L  - Lets you see the map/room again.')
        print('QUESTS     - Lists all your active and completed quests.')
        print('INV        - Lists all the items in your inventory.')
        print('CHECK      - Lets you see an item (or yourself) in more detail.')
        print('NORTH or N - Moves you to the north.')
        print('SOUTH or S - Moves you to the south.')
        print('EAST or E  - Moves you to the east.')
        print('WEST or W  - Moves you to the west.')
        print('QUIT       - Ends the adventure.')
    #if user_input == 'LOOK' or user_input == 'L':
    elif user_input == 'QUESTS':
        if Quest.is_complete(quest_list[0]) == True:
            print("#00: Singing Sword       - PULL the sword from the stone. [COMPLETED]")
        else:
            print("#00: Singing Sword       - PULL the sword from the stone.")
        if Quest.is_complete(quest_list[1]) == True:
            print('#01: Shimmering Shield   - SHINE an old shield unti it shimmers. [COMPLETED]')
        else:
            print('#01: Shimmering Shield   - SHINE an old shield unti it shimmers.')
        if Quest.is_complete(quest_list[2]) == True:
            print('#02: Trembling Tone      - CALM a trembling tone in the workshop. [COMPLETED]')
        else:
            print('#02: Trembling Tone      - CALM a trembling tone in the workshop.')
        if Quest.is_complete(quest_list[3]) == True:
            print('#03: Glistening Goblet   - STEAL a glistening goblet from a distracted denizen. [COMPLETED]')
        else:
            print('#03: Glistening Goblet   - STEAL a glistening goblet from a distracted denizen.')
        if Quest.is_complete(quest_list) == True:
            print("=== All quests complete! Congratulations! ===")
    elif user_input == 'INV':
        print('You are carrying:')
        n = 0
        while n < len(Adventurer(self.inventory)):
            print('-', Adventurer(self.inventory[n]))
            n += 1
        if len(Adventurer(self.inventory)) == 0:
            print('Nothing.')
    elif user_input == 'CHECK':
        t = 0
        question_item = str(input('Check what? '))
        print("")
        if question_item in item_list:
            print(question_item)
        elif question_item == 'ME':
            print('You are an adventurer, with a SKILL of {} and a WILL of {}'.format(Adventurer(self.skill), Adventurer(self.will)))
            print('You are carrying:')
            print()
            if len(Adventurer(self.inventory)) == 0:
                print('Nothing.')
                print()
                print('With your items, you have a SKILL level of {:.0f} and a WILL power of {:.0f}.'.format(Adventurer(self.skill), Adventurer(self.will)))
            while t < len(Adventurer(self.inventory)):
                print(Adventurer(self.inventory[t]))
                print('Grants a bonus of {:.0f} to SKILL.'.format(Item(self.skill_bonus)))
                print('Grants a bonus of {:.0f} to WILL.'.format(Item(self.will_bonus)))
                print()
                print('With you items, you have a SKILL level of', Adventurer(self.skill) + Item(self.skill_bonus), 'and a WILL of', Adventurer(self.will) + Item(self.will_bonus))
                t += 1
    #if user_input == 'NORTH' or user_input == 'N':
    else:
        print('You can''t do that.')
