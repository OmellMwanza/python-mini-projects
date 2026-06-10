import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {
    ROCK: '🪨',
    PAPER: '📄',
    SCISSORS: '✂️'
}

def get_user_choice():
    user_choice = input("Rock, Paper, or Scissors (r/p/s): ").lower()
    if user_choice in emojis:
        return user_choice
    else:
        print("Invalid choice.")


def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}.')
    print(f'Computer chose {emojis[computer_choice]}.')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")

    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == PAPER and computer_choice == ROCK) or
        (user_choice == SCISSORS and computer_choice == PAPER)
    ):
        print("You win!")
    else:
        print("You lose!")

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(list(emojis.keys()))

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        continue_choice = input("Continue? (y/n): ").lower()
        if continue_choice != 'y':
            print("Thanks for playing!")
            break

play_game()