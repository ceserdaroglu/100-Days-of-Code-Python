print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
choice1=input("You're at a cross road. Where do you want to go? Type 'Left' or 'Right' --> ")
if choice1=="left":
    choice2=input("You come to a lake. There is an island in the middle of the lake. Type 'wait' for a boat. Type 'swim' to swim across. --> ")
    if choice2=="wait":
        choice3=input("You arrive at the island unharrred. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? --> ")
        if choice3=="red":
            print("When you opened the red door, a fire started inside. You burned to death with nowhere to run. GAME OVER.")
        elif choice3=="blue":
            print("The beast inside has been waiting for you to open this door for a long time. Bon appetit, beast. GAME OVER.")
        elif choice3=="yellow":
            print("Yellow has always been the right choice. Gold! YOU WON the treasure.")
        else:
            print("You were too late to choose the right door. The chandelier hanging overhead fell on your head and you died. GAME OVER.")
    else:
        print("The trout have been waiting for this moment for centuries. You've been a great meal for them. GAME OVER.")
else:
    print("Oh no! You fell into a big hole and broke all your bones. Sorry dude. GAME OVER. ")

