import random

emojis = {
    'r': '🪨',
    'p': '📄',
    's': '✂️'
}

while True:
    user_choice = input("Rock, Paper, or Scissors (r/p/s): ").lower()
    if user_choice not in emojis:
        print("Invalid choice.")
        continue

    computer_choice = random.choice(list(emojis.keys()))

    print(f'You chose {emojis[user_choice]}.')
    print(f'Computer chose {emojis[computer_choice]}.')

    if user_choice == computer_choice:
        print("Tie!")

    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')
    ):
        print("You win!")
    else:
        print("You lose!")

    continue_choice = input("Continue? (y/n): ").lower()
    if continue_choice != 'y':
        print("Thanks for playing!")
        break
    else:
        continue