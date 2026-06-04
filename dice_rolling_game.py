import random

while True:
    print("Roll the dice? (y/n)")
    roll = input()
    if roll.lower() == 'y':
        dice_roll = random.randint(1, 6)
        dice_roll2 = random.randint(1, 6)
        print(f"({dice_roll}, {dice_roll2})")

    elif roll.lower() == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid Choice.")
