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

def treasury_island():
    print("Welcome to Treasury Island.")
    print("Your mission is to find the treasure.")
    choice1 = input("Where you want to go ? left or right ?\n ").lower()
   
    if choice1 == 'left':
        choice2 = input("You want to swim or wait ?\n").lower()
    
        if choice2 == 'wait':
            choice3 = input("Select a color please. red ? blue ? or yellow ?\n").lower()
            if choice3 == 'blue' or choice3 == 'red':
                print("You chosed the wrong option.Game Over!")
            else:
                print("good choice! You win!")
        else: 
            print("You chosed the wrong direction. Game Over!")
    else: 
        print("You chosed the wrong direction. Game Over!")


if __name__ == "__main__":
    treasury_island()