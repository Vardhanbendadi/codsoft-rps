import random

def main():
    print("Welcome to the game")
    wishes = {
        "0": "paper",
        "1": "rock",
        "2": "Scissors"
    }
    while True:
        while True:
            user_choice = input("Enter your choice (0 for paper, 1 for rock, 2 for Scissors): ")
            if user_choice in wishes:
                break
            else:
                print("Invalid input. Please enter '0', '1', or '2'")
        user_choice = wishes[user_choice]
        computer_input = str(random.randint(0, 2)) 
        computer_choice = wishes[computer_input]

        win_conditions = {
            "paper": "Scissors",
            "rock": "paper",
            "Scissors": "Paper"
        }

        if win_conditions[user_choice] == computer_choice:
            print(f"You won!hurrayyy {user_choice} beats {computer_choice}")
        elif user_choice == computer_choice:
            print(f"It's a tie..{user_choice}")
        else:
            print(f"Computer wins! {computer_choice} beats {user_choice}")

        play_again = input("Play again? (Y/N): ").lower()
        if play_again != "y" and play_again != "n":
            print("Invalid input. Please enter 'Y' or 'N'.")
        elif play_again != "y":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()

