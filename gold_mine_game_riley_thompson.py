from adventurelib import *
Room.items = Bag()

#Room Descriptions
entry_room = Room("""
	You have been closed off from you friends the cave closed behind you.
	Now you must find you way out or die trying.""")

gold_room = Room("""
	You enter a room that is filled to the brim with gold bars.
	You can take them if you dare.""")

open_cave = Room("""
	You enter a cave. In the cave you see a rusty old revolver.
	Do you want to take it?""")

pickaxe_room = Room("""
	There is a room with a pickaxe that you can only carry for short periods of time.
	You must use it to open the door.""")

hallway = Room("""
	You see a hallway has some clay steps with dim lighting to either side.""")

locked_room = Room("""
	The room is empty except for a skeleton on the floor he seems to be holding something?
	""")#Inside room "There is a locked room here that requires some sort of key."

rope_room = Room("""
	There is an empty room that is empty and has a old rope within it.
	""")

elevator = Room("""
	There is an old cable elevator. It is worn down and one of the door have fallen out.
	# Do you want to go up?""")

hallway_2 = Room("""
	As you leave the elevator the cart falls down the shaft behind you.""")

locket_room = Room("""
	The room is empty except for a helm with a golden sword gleaming in the firelight.""")#Locked Room "There is a hole in the door that perfectly fits a locket."

creature_room = Room("""
	There is a mysterious breathing sound in the distance. It is unknown where this sound is coming from.
	You see the way out but you must pass the dragon from here.""")

#Defining Room Connection

entry_room.east = gold_room
entry_room.north = open_cave
entry_room.west = pickaxe_room
pickaxe_room.north = hallway
hallway.east = rope_room
hallway.west = locked_room
hallway.north = elevator
elevator.north = hallway_2
hallway_2.east = locket_room
hallway_2.west = creature_room 

#Defining Items

Item.description = ""#Adds a blank description for each item

gun = Item("a rusty old gun", "a rusty gun", "a gun", "gun")
gun.description = "The gun is an old rusty revolver which must have been down here for over 30 years."

olden_key = Item("olden key", "a key", "the key", "key", "old key")
olden_key.description = "The key is an old key that has been trying to hide underneath the gold bars."

gold = Item("shiny gold", "the gold", "old gold", "gold")
gold.description = "The gold is shiny and looks to be aged like a fine wine."

pickaxe = Item("pickaxe", "old pickaxe,","pick","axe")
pickaxe.description = "The pickaxe is good enough to break a door. However it is is to heavy to carry for long time periods."

locket = Item("locket", "matte locket", "old locket,")
locket.description = "The locket has a image of a man and women smiling togeth presumably man and wife."

rope = Item("rope","old rope")
rope.description = "The rope is old and worn but is quite long and thin."

golden_sword = Item("golden sword","gold sword","sword")
golden_sword.description = "The Golden Sword shimmers in the light as you take it for its helm."

#Defining Bags

open_cave.items.add(gun)
gold_room.items.add(gold)
pickaxe_room.items.add(pickaxe)
locked_room.items.add(locket)
rope_room.items.add(rope)
locked_room.items.add(golden_sword)

#Variables

current_room = entry_room
key_taken = False
inventory = Bag()

#Binds

@when ("go DIRECTION")
def travel (direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)
		print(current_room.exits())

@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}.")
		if t == gold:
			print("There is an old key under the gold")
			gold_room.items.add(olden_key)
	else:
		print(f"You don't see a {item}")

@when("inventory")
@when("show inventory")
@when("what is in my pocket")
def player_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)

@when("look")
def look():
	print(current_room)
	print(f"There are exits in the directions {current_room.exits()}.")
	if len(current_room.items) > 0: #If there are some items in the room
		print("You also see:")
		for item in current_room.items:
			print(item)#print out out each item in the room

'''
@when("search gold")
@when("look at gold")
@when("move gold")
def key_taken():
	global key_taken
	if current_room == gold_room and key_taken == False:
		print("You take the gold and an Old Key it located underneath.")
		current_room.items.add(olden_key)
		key_taken = True #This is False so you cannot search again
	elif current_room == gold_room and key_taken == True:
		print("You have already search the gold.")
	else:
		print("There is no gold to search")'''



def main():
	start()

if __name__ == '__main__':
	main()