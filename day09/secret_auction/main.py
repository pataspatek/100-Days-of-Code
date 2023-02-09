import os
from art import logo


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

print(logo)
print("Welcome to the secret auction.")

bidders = {}
auction = True

while auction:

    name = input("What is your name?: ").capitalize()
    bid = int(input("How much do you want to bid?: $"))
    bidders[name] = bid
    
    more_people = True

    while more_people:
        answer = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if answer == "yes":
            more_people = False
            os.system('cls')
        elif answer == "no":
            print("Thanks for attentind today's auction.")
            auction = False
            break
        else:
            print("Invalid choice.")

find_highest_bidder(bidders)