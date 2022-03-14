"""
fibbonachi = 0,1,1,2,3,5,8,13,21,34
print(f"The first 10 numbers of the Fibonacci sequence are {fibbonachi}") #1
print("\n")

friuts = ['Bannanas', ' Apples', ' Strawberries', ' Oranges']
print(f"My favourite friuts are {','.join(friuts)}") #2
print("\n")

youtubers = ["NoahsNoah", " Jev", " Sidemen", " WILDCAT"]
print(f"My favorite youtubers are {','.join(youtubers)}") #3
print("\n")

favourite_songs = []
favourite_songs.append("Clash")
favourite_songs.append(" Sucker for Pain")
favourite_songs.append(" Hedwig's Theme")
favourite_songs.append(" Friday")
favourite_songs.append(" Crazy Frog Song")
print(f"My favourite songs are {','.join(favourite_songs)}") #4
print("\n")

book = []
book.append("Harry Potter")
book.append(" Ready Player One")
book.append(" Green Eggs and Ham")
book.append(" Maze Runner")
book.append(" Star Wars Novels")
print(','.join(book)) #5
print("\n")
"""

pizza_toppings = []
user_pt = input("Add a pizza topping\n")
if user_pt != "":
	pizza_toppings.append(user_pt)
user_pt = input("Add a pizza topping\n")
if user_pt != "":
	pizza_toppings.append(user_pt)
user_pt = input("Add a pizza topping\n")
if user_pt != "":
	pizza_toppings.append(user_pt)
user_pt = input("Add a pizza topping\n")
if user_pt != "":
	pizza_toppings.append(user_pt)
user_pt = input("Add a pizza topping\n")
if user_pt != "":
	pizza_toppings.append(user_pt)
user_pt = input("Add a pizza topping\n")
if user_pt != "":
	pizza_toppings.append(user_pt)
print(','.join(pizza_toppings))