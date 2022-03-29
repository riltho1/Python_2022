from adventurelib import *

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
	There is a locked room here that requires some sort of key.
	""")

rope_room = Room("""
	There is an empty room that is empty and has a old rope within it.
	""")

elevator = Room("""
	There is an old cable elevator. It is worn down and one of the door have fallen out.
	# Do you want to go up?""")

hallway_2 = Room("""
	As you leave the elevator the cart falls down the shaft behind you.""")

locket_room = Room("""
	There is a hole in the door that perfectly fits a locket.""")

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



#Binds

@when ("go DIRECTION")
def travel (direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)
		print(current_room.exits())

@when("look")
def look():
	print(current_room)
	print(f"There are exits in the directions {current_room.exits()}.")
	if len(current_room.items) > 0: #If there are some items in the room
		print("You also see:")
		for item in current_room.items:
			print(item)#print out out each item in the room



def main():
	start()

if __name__ == '__main__':
	main()