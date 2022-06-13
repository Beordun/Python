import random

while True:
    choices = ["rock","paper","scissors"]

    CPU = random.choice(choices)
    player = None

    while player not in choices:
        
        player = input("R, P, or S: ").lower()
        print("The selected option is not available, enter from the value below")

    if player == CPU:
        print("CPU: ",CPU)
        print("player: ",player)
        print("draw-draw")

    elif player == "rock":
        if CPU == "paper":
            print("CPU: ", CPU)
            print("player: ", player)
            print("Breakfast na for everyone, you lose!")
        if CPU == "scissors":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You win, get a drink!")

    elif player == "scissors":
        if CPU == "rock":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You lose this time!")
        if CPU == "paper":
            print("CPU: ", CPU)
            print("player: ", player)
            print("Rock don crash paper, you Win!")

    elif player == "paper":
        if CPU == "scissors":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You don lose ths one!")
        if CPU == "rock":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You win!")

   
        break

print("Odabo, you self try!")