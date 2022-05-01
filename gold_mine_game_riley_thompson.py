from adventurelib import *
Room.items = Bag()

import sys

#Adding Directions

Room.add_direction("up","down")

print("You have decided to go on a trip to an abandoned gold mine with your friends. You get on the plane and head off to Spain. You have chanrged ahead of your friends and have been barricaded in on oppposite sides. You must find a way to get out. ")

#Room Descriptions
#Update the later
entry_room = Room("""
	You have been closed off from you friends the cave closed behind you.
	Now you must find you way out or die trying.
	You can PICK UP/TAKE items that you find around the mine.""")

gold_room = Room("""
	You enter a room that is filled to the brim with gold bars.
	You can take them if you dare.""")

open_cave = Room("""
	You enter a cave. In the cave you see a rusty old revolver.
	Do you want to take it?""")

broken_room = Room("""
	There is a door here. However it seems to have been hacked at and destroyed. Weird.""")

hallway = Room("""
	You see a hallway has some clay steps with dim lighting to either side.""")


locked_room = Room("""
	The room is empty except for a skeleton on the floor he seems to be holding something?
	""")#This room is locked from outside unless you have the Olden Key

rope_room = Room("""
	There is an empty room that is empty and has a old rope within it.
	""")

elevator = Room("""
	There is an old cable elevator. It is worn down and one of the doors seem to have fallen off.
	Do you want to go up?""")

hallway_2 = Room("""
	As you leave the elevator the cart falls down the shaft behind you. You are stuck up here unless you can find a way to get back down.""")

locket_room = Room("""
	The room is empty except for a helm with a golden sword gleaming in the firelight.""")#This room is locked unless you have the Locket

creature_room = Room("""
	There is a mysterious breathing sound in the distance. It is unknown where this sound is coming from.
	You see the way out but you must pass the dragon from here.
	Do you attack it or do you try to sneak past.
	What will you ATTACK WITH.""")

"""exit_room = Room(""
	You kill the mysterious creture and manage to find you way out of the cave.
	Well done you are now free to go."")"""
	#Didn't need this room


#Defining Room Connection

#The rooms only need to be connected one way.
entry_room.east = gold_room
entry_room.north = open_cave
entry_room.west = broken_room
broken_room.north = hallway
hallway.east = rope_room
hallway.west = locked_room
hallway.north = elevator
elevator.up = hallway_2
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

locket = Item("locket", "matte locket", "old locket,")
locket.description = "The locket has a image of a man and women smiling togeth presumably man and wife."

rope = Item("rope","old rope")
rope.description = "The rope is old and worn but is quite long and thin."

golden_sword = Item("golden sword","gold sword","sword")
golden_sword.description = "The Golden Sword shimmers in the light as you take it for its helm."

#Defining Bags

#Scrapped the Pickaxe
open_cave.items.add(gun)
gold_room.items.add(gold)
'''pickaxe_room.items.add(pickaxe)'''
rope_room.items.add(rope)


#Variables

#Variables are used to assign values
current_room = entry_room
key_taken = False
locket_taken = False
rope_taken = False
sword_taken = False
inventory = Bag()


#Binds

#Binds make the game move between rooms and look around. It gives the user control.
@when ("go DIRECTION")
def travel (direction):
	global current_room
	global locket_taken
	if current_room == hallway and direction == 'west' and key_taken == False:
		print("The door is locked")	
		return
	elif current_room == hallway and direction == 'west' and key_taken == True:
		locked_room.items.add(locket)
		locket_taken = True

	if current_room == hallway_2 and direction == 'east' and locket_taken == False:
		print("The door is locked")	
		return
	elif current_room == hallway_2 and direction == 'east' and locket_taken == True:
		locket_room.items.add(golden_sword)

	if current_room == hallway_2 and direction == 'down' and rope_taken == False:
		print("The cart snapped and fell down the elevator shaft. You would need a rope or something to get back down there.")
		return
	elif current_room == hallway_2 and direction == 'down' and rope_taken == True:
		print("You use the rope to get up and down between the elevator")

		#Rope and elevator works room description needs to change when you go down with rope

	if current_room == creature_room and direction == 'east':
		print("When you came through the door it slammed loudly behind you unable to be opened")
		return
	#This locks the door behind you in the final room




	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)
		print(current_room.exits())
	else:
		print("You cannot go that way.")
#Testing code
	"""elif current_room in current_room.exits() and elevator_taken == True:
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room.exits())"""

	"""if current_room == hallway_2 and direction in current_room.exits() == 'down':
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room.exits())"""

	


@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	global key_taken
	global rope_taken
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}.")
		if t == gold:
			print("There is an old key under the gold")
			gold_room.items.add(olden_key)
		#When these items are in your inventory the variables the corispond to become true
		if t == olden_key:
			key_taken = True
		if t == rope:
			rope_taken = True
	else:
		print(f"You don't see a {item}")

#This bind is used to end the game and give you one of 2 endings
@when("attack with ITEM")
@when("use ITEM")
def attack_with(item):
	if inventory.find(item) == golden_sword and current_room == creature_room:
		print("You use the Golden Sword to kill the creture")
		sys.exit("You later found your way out after killing the mysterious creture and managed to regroup with you friends. You will never be the same after that day.")
	else:
		print("You attacked the creature and instantaniously died")
		sys.exit("Your friends later managed to get a search party in the cave to find you and your body was found dead with deep wounds. 'What could have done this?' They think to themselves.")




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

@when("look at ITEM")
@when("inspect ITEM")
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying an {item}")


def main():
	start()

if __name__ == '__main__':
	main()