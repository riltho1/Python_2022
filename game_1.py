from adventurelib import *
Room.items = Bag()

#Room Descriptions
space = Room("""
	You are drifting in space. It feels very cold.
	A slate-blue starsharp sits completely silently to your left,
	its airlock open and waiting.
	""")

spaceship = Room("""
	The bridge if the spaceship is shiny and white, with thousands
	of small, red, blinking lights.
	""")

quaters = Room("""
	The futuristic quaters look very cozy .
	They have individual beds that look out at the stars.
	""")

mess_hall = Room("""
	The canteen is rather empth  with plates on the tables and the bar.
	""")

hallway = Room("""
	The Halls are very wide and well lit yet there is still no one here.
	""")

bridge = Room("""
	The control room has many tablets and electronics all over.
	There is a lot of noise coming from the next room over.
	""")

cargo = Room("""
	The cargo room has rifles locked up as well as some precious cargo.
	""")

docking = Room("""
	The docking bay has one extra ship in it.
	""")

escape_pods = Room("""
	Woosh there goes last escape pod you are stuck.
	""")

#Creating Room Connections

spaceship.east = hallway
spaceship.south = quaters
hallway.east = bridge
hallway.north = cargo
quaters.east = mess_hall
mess_hall.north = hallway
bridge.south = escape_pods
cargo.east = docking

#Defining Items
Item.description = "" #this adds a blank description to each item

knife = Item("a dirty knife","knife")
knife.description = "The knife has a dull sheen to it but it looks rather sharp."

red_keycard = Item("a red keycard","keycard","red card","red card")
red_keycard.description = "It's a red keycard. It probably opens a door or a locker."

spacesuit = Item("spacesuit","old worn spacesuit")
spaceship.description = "The spacesuit is quite old and worn out."

music_player = Item("music player","apple music player")
music_player.description = "There is an old Apple Music Player that hs some songs from the 2000s"

#Defining Bags

mess_hall.items.add(red_keycard)
cargo.items.add(knife)
docking.items.add(spacesuit)
quaters.items.add(music_player)

@when ("go DIRECTION")
def travel (direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)
		print(current_room.exits())


#Variable
current_room = space
invetory = Bag()

#Binds
@when("enter airlock")
@when("enter spacehip")
@when("enter ship")
def enter_spaceship():
	global current_room
	#check if this action can be done
	if current_room is not space:
		say("There is no airlock here")
		return
	else:
		current_room = enter_spaceship
		print("""
		You heave yourself into the spaceship and
		slam you hand on the button to close the door.
		""")

@when("look")
def look():
	print(current_room)
	print(f"There are exits in the directions {current_room.exits()}.")
	if len(current_room.items) > 0: #If there are some items in the room
		print("You also see:")
		for item in current_room.items:
			print(item)#print out out each item in the room

@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current.room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}.")
	else:
		print(f"You don't see a {item}")

@when("inventory")
@when("show inventory")
@when("what is in my pocket")
def player_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)

def main():
	start()

if __name__ == '__main__':
	main()