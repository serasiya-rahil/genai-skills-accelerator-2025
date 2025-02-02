import random

# Step 1: Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Initialize variables
attempts = 0
max_attempts = 10  # Limit attempts to 10

# Step 2: Prompt the user for guesses using a while loop
print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100.")

while attempts < max_attempts:
    # Get the user's guess
    guess = int(input(f"Guess the number (between 1 and 100): "))
    
    attempts += 1  # Increment the attempts counter
    
    # Step 3: Check the guess and give feedback
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break  # Exit the loop when the guess is correct

# If the user fails to guess correctly in 10 attempts
if guess != number_to_guess:
    print(f"Game over! The correct number was {number_to_guess}. Better luck next time!")
