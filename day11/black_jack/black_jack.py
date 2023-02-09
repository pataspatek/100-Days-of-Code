import random
from art import logo
from deck import deck 
import os

game = True
while game:
    print(logo)

    player_cards = []
    dealer_cards = []
    player_value = 0
    dealer_value = 0

# Dealing cards starts with the player. Each card is removed from the deck after draw. 
    for index, item in enumerate(deck):
        if index in range(4):
            item = deck.pop(random.choice(range(len(deck))))

# First and third card goes to the player. Their values are added into player_value.
            if index == 0 or index == 2:
                player_value += item
                player_cards.append(item)

# Second and forth card goes to the dealer. Their values are added into dealer_value. 
            elif index == 1 or index == 3:
                dealer_value += item
                dealer_cards.append(item)

# While player_value is less than 21, he can draw another card.
# If the player_value is equal to 21, he won immediately. 
# At this point, player does not see the dealer's second card. 
    while player_value < 21:
        print(f"\nYour hand: {player_cards} your current value is: {player_value}.")
        print(f"Dealer's hand: [{dealer_cards[0]}, ??]\n")

        hit_stand = input("Do you want another card? 'y' or 'n': ")
        if hit_stand == "y":
            item = deck.pop(random.choice(range(len(deck))))
            player_value += item
            player_cards.append(item)

# If the player_value exeeds 21 after drawing another card. Value of ace becomes 1 instead of 11.
            if player_value > 21 and 11 in player_cards:
                ace = player_cards.index(11)
                player_cards[ace] = 1
                player_value -= 10
        else: 
            break

# While player_value is less than 21 (game didn't end after player's turn) and the dealer_value is less than 17, dealer keeps drawing.
    while player_value < 21 and dealer_value < 17:
        item = deck.pop(random.choice(range(len(deck))))
        dealer_value += item
        dealer_cards.append(item)

# Value of ace changes to 1 if the dealer_value exeeds 21 after drawing additional cards. 
        if dealer_value > 21 and 11 in dealer_cards:
            ace = dealer_cards.index(11)
            dealer_cards[ace] = 1
            dealer_value -= 10

# Reveals both hands after adding additional cards based on conditions above.
    print(f"\nYour final hand: {player_cards} final value is: {player_value}.")
    print(f"Dealer's final hand: {dealer_cards} final value is: {dealer_value}.")

# Decides who is the winner based on the hand value comparison. 
    if player_value == dealer_value:
        print("Draw 🙃\n")
    elif player_value == 21:
        print("Win with a Blackjack 😎\n")
    elif dealer_value == 21:
        print("Lose, opponent has Blackjack 😱")
    elif player_value > 21:
        print("You went over. You lose 😭")
    elif dealer_value > 21:
        print("Opponent went over. You win 😁\n")
    elif player_value > dealer_value:
        print("You win 😃\n")
    else:
        print("You lose 😤\n")

# Asks the user if he wants to play another game.
# If yes, clears the console and start over the whole loop. 
# If not, game = False will break the while loop and end the programme. 
    another_game = input("\nDo you want to play antoher game? 'y' or 'n': ")
    if another_game == "y":
        os.system('cls')

    elif another_game == "n":
        game = False

print("Thanks for playing Blackjack!")