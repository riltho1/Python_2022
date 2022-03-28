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

locket_room = Room("""
	There is a hole in the door that perfectly fits a locket.""")


def main():
	start()

if __name__ == '__main__':
	main()