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

print("You're at a cross road. Where do you want to go?")
direction = input('''''''Type "left" or "right". ''')
if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")

    waitorswim = input('''Type "wait" to wait for a boat. Type "swim" to swim across. ''')
    if waitorswim == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")

        doors = input("One red, one yellow, one blue. which colour do you choose? ")
        if doors == "red":
            print("it's a room full of fire. Game over!")
        if doors == "blue":
            print("You enter a room full of beasts. Game over!")
        if doors == "yellow":
            print("Congratulations! You found the treasure! You win!")
        else:
            print("Game Over!")
    else:
     print("You have been attacked by a pack of piranhas. Game over!")

else:
    print("You have fallen into a hole. Game over!")
