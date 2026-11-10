import random
from operator import truediv

low = 1
high = 100
answer = random.randint(low, high)

guesses = 0
is_running = True

print("Welcome to the random number guessing game!")
print("")
print(f"Select a number between {low} and {high}")
print("")
while is_running:
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}!")
        elif guess < answer:
            print("Too low!")
        elif guess > answer:
            print("Too high!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"You guessed {guesses} times!")
            is_running = False
    else:
        print("Please enter a number!")
        print(f"Select a number between {low} and {high}")