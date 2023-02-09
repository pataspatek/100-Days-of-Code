import random
from art import logo
import os

def set_number_attempts(difficulty):
    if difficulty == "hard":
        return 5
    else:
        return 10

def set_number_range(difficulty):
    if difficulty == "hard":
        return random.randint(1, 1000)
    else:
        return random.randint(1, 100)

game = True
while game:
    print(logo)
    print("Welcome to the Number Guesing Game!\n")
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = set_number_attempts(difficulty)
    number = set_number_range(difficulty)
    
    low = 1
    if difficulty == "hard":
        high = 1000
    else:
        high = 100

    guess = 0
    while guess != number:
        print(f"You have {attempts} attempts to guess the number.")
        print(f"The number is between {low} and {high}\n")

        guess = int(input("Make a guess: "))

        if guess > number:
            print("Too high.")
            high = guess
            attempts -= 1
                        
        elif guess < number:
            print("Too low.")
            low = guess
            attempts -= 1
            
        else: 
            print("Congratz, you guessed the correct number.")
    
        if attempts == 0:
            print("No more attempts")
            print(f"The number was {number}.")
            break
        
    if input("\nWould you like to play one more time? Type 'y' or 'n': ") == "n":
        break
    else:
        os.system('cls')
