import random

computer = ["Rock", "Paper", "Scissors"]
print("Rock paper scissors!")
game = int(input("Play? 1 for yes, 2 for no: "))

if game == 2:
    print("Okay, then why even open the game?")
    exit()

choice = int(input("1 for rock, 2 for paper, 3 for scissors: "))

if choice == 1:
    choice = "Rock"
elif choice == 2:
    choice = "Paper"
elif choice == 3:
    choice = "Scissors"
else:
    print("Invalid choice. Please choose a number between 1 and 3.")
    exit()

randomChoice = random.choice(computer)
print(randomChoice)

if choice == randomChoice:
    print("Tie!")
elif (choice == "Rock" and randomChoice == "Paper") or \
     (choice == "Paper" and randomChoice == "Scissors") or \
     (choice == "Scissors" and randomChoice == "Rock"):
    print("You lost!")
else:
    print("You win!")
