import random

def get_user_choice():
    while True:
        try:
            choice = int(input("1 for Rock, 2 for Paper, 3 for Scissors: "))
            if choice in (1, 2, 3):
                return choice
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    computer = ["Rock", "Paper", "Scissors"]
    print("Rock, Paper, Scissors!")

    while True:
        game = input("Play? (yes/no): ").strip().lower()
        if game == "no":
            print("Thanks for playing!")
            break
        elif game == "yes":
            user_choice = get_user_choice()
            computer_choice = random.choice(computer)
            print(f"Computer chose {computer_choice}")

            if user_choice == computer.index(computer_choice) + 1:
                print("It's a tie!")
            elif (user_choice == 1 and computer_choice == "Scissors") or \
                 (user_choice == 2 and computer_choice == "Rock") or \
                 (user_choice == 3 and computer_choice == "Paper"):
                print("You win!")
            else:
                print("Computer wins!")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    play_game()
