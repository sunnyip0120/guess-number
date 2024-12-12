import random

print("Welcome to Guess the Number!")
lowest = 1
highest = 100
secret_number = random.randint(lowest, highest)
attempts = 0

def guess_the_number():
    global lowest, highest, attempts  # Declare all global variables at the start
    while True:
        try:
            guess = int(input(f"Guess a number between {lowest} and {highest}: "))
            attempts += 1  # Correctly increment attempts

            if guess < lowest or guess > highest:
                print(f"Please guess a number within the range {lowest} to {highest}.")
            elif guess < secret_number:
                print("Too low! Try again.")
                lowest = guess  # Update the lowest boundary
            elif guess > secret_number:
                print("Too high! Try again.")
                highest = guess  # Update the highest boundary
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    guess_the_number()
