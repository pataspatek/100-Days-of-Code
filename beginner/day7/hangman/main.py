import random
import os
from words import words
from pictures import stages, logo

game = True
while game == True:

    chosen_word = random.choice(words)
    word_length = len(chosen_word)
    pokracovat = False
    end_of_game = False
    lives = 6
    used_words = []
    display = []

    for i in chosen_word:
        if i == "-":
            display += "-"
        elif i == " ":
            display += " "
        else:
            display += "_"

    print(logo)
    print(f"\n{' '.join(display)}")


    while end_of_game == False:
        guess = input("\nGuess a char: ").lower()
    
        os.system('cls')

        print(logo)

        if guess not in used_words and len(guess) == 1:
            used_words += guess

        
        if guess in display:
            print(f"You've already guessed '{guess}'. Try different one.")

        if len(guess) == 1:
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
                elif letter == "-":
                    display[position] = "-"
                elif letter == " ":
                    display[position] = " " 
        elif len(guess) != 1:
            print("Only one letter please!")
        
        print(f"\n{' '.join(display)}")

        if guess not in chosen_word and len(guess) == 1:
            print(f"\nLetter '{guess}' is not in the word. You loose a life.")
            lives -= 1 
            if lives == 0:
                end_of_game = True
                pokracovat = True
                print(f"You loose!\nThe word was {chosen_word}.")
            print(stages[lives])
            print(f"Used words: {', '.join(used_words)}")  
        
        elif guess not in chosen_word and len(guess) != 1:
            print(stages[lives])
            print(f"Used words: {', '.join(used_words)}")  
            pass

        elif "_" not in display:
            end_of_game = True
            pokracovat = True
            print("\nCONGRATULATIONS YOU WIN!")

        else:
            print()
            print()
            print(stages[lives])
            print(f"Used words: {', '.join(used_words)}")  
    
    while pokracovat == True:
        answer = input("\nWould you like to play another one? 'yes' or 'no' ")
        if answer == "yes":
            pokracovat = False
            os.system('cls')
        elif answer == "no":
            pokracovat = False
            end_of_game = False
            game = False
        else:
            print("Invalid input.")

print("Thanks for playing!")