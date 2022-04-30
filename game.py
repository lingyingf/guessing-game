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

print("Hello! What is your name? ")
name = input("> ")
print("Hi", name, "welcome to the game!")