print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_path = input("Choose your path, left or right?\n")
if first_path.lower() in ["left", "l"]:
    print("You traverse a dense jungle when suddenly you get ensnared in a rope trap but you manage to escape.")
else:
    print("You run into a small village of settlers who are having a feast.\nThey invite you and you have a great time until you fall asleep. You wake up to being tied up hanging above a boiling cauldron.\nThe settlers turned out to be vicious cannibals and have trapped you. You are eaten, Game Over.")
    exit()
second_path = input("You continue through the jungle until you come across a lake. Swim or wait?\n")
if second_path.lower() in ["wait", "w"]:
    print("You wait for while until you see a small boat down the shoreline. You use the boat to traverse the lake.")
else:
    print("You attempt to swim across when suddenly you are dragged under by sirens, they drown and eat you. Game Over.")
    exit()
third_path = input("You reach the other side and approach the abandoned mansion. You enter and begin to search around.\nYou run into a large room that has three large doors. One red, one yellow and one blue, which door?\n")
if third_path.lower() in ["red", "r"]:
    print("You enter a large room full of torches when suddenly a dragon appears.\nIt engulfs you in flames and you die. Game Over.")
    exit()
elif third_path.lower() in ["yellow", "y"]:
    print("You enter a room with a yellow glow in the dark mist. You continue on when you notice a bright light of a bunch of knights armor scattered around.\nThe armor begin to assemble into a giant iron knight. It impales you with its spear and you die. Game Over.")
    exit()
elif third_path.lower() in ["blue", "b"]:
    print("You enter a room with a large waterfall and stone bridge. You see a treasure chest on an alter.\nYou begin to cross the bridge when suddenly it begins to crumble behind you.\nYou race across the bridge and just barely make it. You grab the chest and find a gem that can teleport you anywhere.\nYou win!")
else:
    print("You decide not continue through any of the doors and leave. You find a horde of zombies outside has surrounded you.\nThey kill and eat you. Game Over.")
