# Random Number Guessing Game - Generates a random number for the user to guess!
# CTI-110
# Sigrid Olive
# 6/27/2017

import random

# explains what program does
print("This program is a Random Number Guessing game.")
print("It will randomly generate a number for the user to guess.")
print("\n")



def main():
    play_game()
    while play_again():
        play_game()

def play_game():
    # sets a random number
    number = random.randint(1,100)
    print("Generating number...")
    print("\n")
    guess = int(input("What do you think the number is? "))
    print("\n")
    print("The number was actually: ", number)
    
    if guess > number:
        print("Too high, try again!")
    elif guess < number:
        print("Too low, try again!")
    else:
        print("Congratulations! You guessed the correct number!")
        
def play_again():
    answer = input("Do you want to play again? [Y/N] ")
    if answer == 'y' or answer == 'Y':
        return True
    else:
        print ("\n")
        print("Thanks for playing!")
        return False

main()
