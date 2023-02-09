from art import logo, vs
from data import data
import random
import os

score = 0
n1 = random.randint(0, len(data) -1)
first_number = data[n1]["follower_count"]
first_profile = data[n1]["name"] + " a " + data[n1]["description"] + " from " + data[n1]["country"]
data.remove(data[n1])

game = True
while game:
    print(logo)

    if len(data) == 0:
        print("No more accounts to compare!")
        break
        
    print(f"\nCurrent score: {score}\n")

    print(f"Compare A: {first_profile}")

    n2 = random.randint(0, len(data) -1)
    seccond_number = data[n2]["follower_count"]
    seccond_profile = data[n2]["name"] + " a " + data[n2]["description"] + " from " + data[n2]["country"]
    data.remove(data[n2])

    print(vs)

    print(f"Against B: {seccond_profile}")

    progress = True
    while progress:
        guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

        if guess == "a":
            if first_number > seccond_number:
                score += 1
                progress = False
            else:
                progress = False
                game = False

        elif guess == "b":
            if seccond_number > first_number:
                score += 1
                progress = False
            else:
                progress = False
                game = False

        else: 
            print("You gotta choose one! Try again. ")
            continue

    first_profile = seccond_profile
    first_number = seccond_number

    os.system('cls')

print(logo)
print(f"Final score: {score}.")