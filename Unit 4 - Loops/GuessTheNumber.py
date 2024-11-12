import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)
user_input = None  # Initialize user_input with a different type
tries = 0

while number != user_input:
    try:
        user_input = int(input("Guess the number between 1 and 100\n>"))
    except:
        print("Hmm... That's not right...")

        
    if user_input < number:
        print("Higher! Try again.")
        tries += 1
    elif user_input > number:
        print("Lower! Try again.")
        tries += 1
    else:
        print("You've guessed the number! 🎉")
        print(f"You have tried {tries} times")

print("Game over!")