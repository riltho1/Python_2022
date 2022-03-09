#Input
"""
input("Press any key, press enter. ") #1
input("Type your name and enter. ") #2
input("Type your age and enter. ") #3
print("\n")

#Stored Inputs
user_name = input("Enter your name. ") #4
user_age = input("Enter your age. ") #5
favourite_movie = input("What is your favourite movie? ") #6
book_name = input("What's your favourite book? ") #7
user_adjective = input("Name an adjective. ") #8
user_noun = input("Name a noun. ") #9
user_verb = input("Name a verb. ") #10
print("\n")

print(f"Hello there {user_name}. ")
print(f"You are {user_age}. ")
print(f"{favourite_movie} is good.")
print(f"{book_name} is bad though.")
print(f"{user_adjective} is a very bad describing word.")
print(f"{user_noun} is a good word. ")
print(f"{user_verb} is a good word. ") #11

#Conversion to Integers
user_age = int(input(f"How old are you?\n")) #12
print(f"You will be {user_age+10} in 10 years") #13
print(f"You were born in {2022 - user_age}") #14

#Division
apple = int(input(f"How many apples do you have?\n")) #15
friends = int(input(f"How many friends do you have?\n")) #16
print(f"You can share {apple//friends} apples between you friends.\n") #17
pizza = int(input(f"How many pizzas do you want?\n")) #18
pizzas_eaten = int(input(f"How many people are you feeding?\n")) #19
print(f"Each person gets {pizza*8//pizzas_eaten} slices\n") #20

user_money = int(input(f"How much money do you have?\n")) #21
tv_cost = int(input(f"How much does a tv cost?\n")) #22
print(f"You will have {user_money-tv_cost} dollars after you buy the TV.\n") #23
print(f"The TV will cost {tv_cost*0.8} if there is a 20% off sale\n") #24
user_bitcoins = float(input(f"How many bitcoins do you have\n")) #25
bitcoin_cost = (55661.97) #26
print(f"You have {user_bitcoins} that is worth ${user_bitcoins*bitcoin_cost}") #27

user_earnings = int(input(f"How much money do you earn a week?\n")) #28
tax_rate = float(input(f"What is the current tax rate as a decimal?\n")) #29
print(f"After tax you earn ${user_earnings-user_earnings*tax_rate}") #30
"""
book = input("Name a book.\n") #31
print("\n")
print(book.upper())
print(book.lower())
print(book.title()) #32
print("\n")

number = int(input("Give me a number.\n")) #33
print(book*number) #34