import random

while True:
    youstr = input("Enter your option (s for Snake, w for Water, g for Gun) or 'exit' to quit: ")
    
    if youstr.lower() == 'exit':
        print("Thanks for playing! Game ended.")
        break

    youDict = {
        "s": 1,  
        "w": -1, 
        "g": 0   
    }

    reverseDict = {
        1: "Snake",
        -1: "Water",
        0: "Gun"
    }

    computer = random.choice([1, -1, 0])

    you = youDict.get(youstr.lower()) 

    if you is None:
        print("Invalid input! Please choose 's' for Snake, 'w' for Water, or 'g' for Gun.")
    else:
        print(f"You chose {reverseDict[you]} and the computer chose {reverseDict[computer]}.")

        # Game logic
        if computer == you:
            print("It's a draw!")
        elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
            print("You win!")
        else:
            print("You lose!")
