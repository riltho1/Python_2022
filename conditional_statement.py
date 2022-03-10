#If and Elif
"""
ice_cream = int(input("How many Ice Cream's do you want?\n"))
if ice_cream < 20:
	print("Coming right up!")
elif ice_cream > 20:
	print("We don't have enough Ice Cream in stock") #1
print("\n")

travel_distance = int(input("How far do you plan to travel(Just number)?\n"))
if travel_distance < 200:
	print("Safe Travels!")
elif travel_distance >= 200:
	print("Remember to fill your petrol.") #2
print("\n")

user_age = int(input("How old are you?\n"))
if user_age < 18:
	print("You are a minor")
elif user_age >= 18:
	print("You are an adult") #3
print("\n")

user_movie = input("What is your favourite film\n")
if user_movie == "Lord of the Rings":
	print("You have excellent taste.")
else:
	print("Lord of the Rings is superior") #4
print("\n")

darth_plagueis = input("Did you ever hear the tragedy of Darth Plagueis The Wise? \n")
if darth_plagueis.lower() == "no":
	print("I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.\n")
elif darth_plagueis.lower() == "yes":
	print("You must be a fan?") #5
	print("\n")

who_directed = input("Do you know the director of 'Passion of the Christ'?\n")
if who_directed.lower() == "mel gibson":
	print("Correct!")
else:
	print("This is incorrect the awnser is Mel Gibson") #6
print("\n")
"""
#This is a script that asks questions and increases your score if you awnser correct
score = 0
qustion_1 = input("Whio won the 2019 Champions League?\n")
if qustion_1.lower() == "liverpool":
	score+=1
	print(f"Correct that's {score} points.\n")
else:
	print(f"Wrong the awnser is Liverpool ypu have {score} points.\n")


question_2 = input("Who won the 2010 FIFA World Cup?\n")
if question_2.lower() == "spain":
	score+=1
	print(f"Correct you have {score} points.\n")
else:
	print(f"Wrong the awnser is Spain you have {score} points.\n")


question_3 = input("Who won the 2015/16 Premier League?\n")
if question_3.lower() == "leicester city":
	score+=1
	print(f"Correct you have {score} points.\n")
else:
	print(f"Wrong the awnser is Leicester City you have {score} points.\n")


question_4 = input("Who has won the most Champions League titles?\n")
if question_4.lower() == "real madrid":
	score+=1
	print(f"Correct you have {score} points.\n")
else:
	print(f"Wrong the awnser is Real Madrid you have {score} points.\n")


question_5 = input("What national team won Euro 2016?\n")
if question_5.lower() == "portugal":
	score+=1
	print(f"That's the right awnser you have {score} points.\n")
else:
	print(f"Wrong the awnser is Portugal you have {score} points.\n") #7
