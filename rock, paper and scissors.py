import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    # creating a while loop to be able to select only 3 types of inputs
    # lower() will accept inputs at any letter size

    while player not in choices:
        player = input("rock paper or scissors? ").lower()


    def result():
        print("computer: ", computer)
        print("You: ", player)


    if player == computer:
        result()
        print("Stalemate!")
    elif player == "rock":
        if computer == "paper":
            result()
            print("Paper beat rock! Computer wins")
        else:
            result()
            print("Paper beat rock! Player wins")
    elif player == "paper":
        if computer == "scissors":
            result()
            print("Scissors beat paper! Computer wins")
        else:
            result()
            print("Scissors beat paper! Player wins")
    elif player == "scissors":
        if computer == "rock":
            result()
            print("Rock beats scissors! Computer wins")
        else:
            result()
            print("Scissors beat paper! Player wins")

    print(" ")

    # creating playing again section

    again = input("Do you want to play again, type y or n: ").lower()

    if again != "yes" and again != "y":
        break
