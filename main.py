import random

# Number guessing game
print("\nWelcome to the number guessing game!\n")
print("Pick a range of numbers.\n")
print("The computer will choose a random number from the range and you will guess the number the computer chose.\n")
print("You have three chances to guess the number. Good luck!\n")

# Global variables:
min_number = int(input("Pick a number for the minimum of the range: "))
max_number = int(input("Pick a number for the maximum of the range: "))

# Get minimum range
def min_of_range():
    return min_number


# Get maximum range
def max_of_range():
    return max_number


# Computer chooses random number from range
def computer_number():
    number_to_guess = random.randint(min_of_range(), max_of_range())
    return number_to_guess


# User has three chances to guess the computer number
def player_guesses_number():
    the_number = computer_number()
    print("The computer has picked a number within your range. You have 3 chances to guess what it is.")

    for number in range(3):
        player_guess = int(input("Guess the number: "))
        win = (player_guess == the_number)
        if win:
            print(f"You have guessed {player_guess}. That is correct! YOU WIN!!!!")
            break
        else:   
            print(f"You have guessed {player_guess}. That is incorrect.")

    if player_guess != the_number:
        print(f"You lose! The correct number was {the_number}.")


player_guesses_number()