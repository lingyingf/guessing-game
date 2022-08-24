"""A number-guessing game."""

# Put your code here
# Guessing Game: 
'''1) Assign random number
2) intake the guessed number - and compare it to the random number using > < to see if guess
is too high or low and then output if it is too high or too low - loop this process until the 
corret number is guessed. guessed number == random number --> break loop
3) Create a counter variable to count how many guesses.  count_guess= 0
when a guess happens, we will += 1 to the count_guess variable
4) When loop ends, print - good job {name} you guessed in {count_guess} tries!
'''
import random

print("Hello! What is your name? ")
name = input("> ")
print("Hi", name, "welcome to the game!Please add a number between 1 - 100")
guessed_number = int(input("> "))
if guessed_number < 1 or guessed_number > 100:
    print("Not within number range. Please try again")
    guessed_number = int(input("> "))
random_number = random.randint(1,101)

def guess(guessed_number):
    guess_count = 1
    while guessed_number != random_number:
        if guessed_number < 1 or guessed_number > 100:
            print("Not within number range. Please try again")
            guessed_number = int(input("> "))
        elif guessed_number > random_number:
            print("Too high. Guess again.")
            guessed_number = int(input("> "))
            guess_count += 1
        elif guessed_number < random_number:
            print("Too low. Guess again.")
            guessed_number = int(input("> "))
            guess_count += 1
        else:
            print("Not a valid entry. Please guess again.")
            guessed_number = int(input("> "))
    print(f"You win! You guessed the correct number in {guess_count} guesses!")


guess(guessed_number)
    
            
