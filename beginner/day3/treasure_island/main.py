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

level1 = True

while level1:
    road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'.\n").lower()
        
    if road == "left":
        print("You chose wisely!")
        level1 = False
        level2 = True
        
    elif road == "right":
        print("You fell into a hole.")
        exit("Game over!")

    else:
        print("Choose available option.")

while level2:
    lake = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
        
    if lake == "wait":
        print("You chose wisely!")
        level2 = False
        level3 = True

    elif lake == "swim":
        print("You were attacked by trout.")
        exit("Game over!")

    else:
        print("Choose available option.")

while level3:
    door = input("You arrive at the island unharmed. There is a house with 3 doors. Red, yellow, blue. Which color do you choose.\n").lower()
       
    if door == "red":
        print("You got burned by fire.")
        exit("Game over!")

    elif door == "blue":
        print("You got eaten by beasts.")
        exit("Game over!")

    elif door == "yellow":
        print("Congtratulations. You found the treasure!")
        exit("Game over!")
            
    else:
        print("Choose available option")
        continue