import random

rock_pic = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper_pic = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors_pic = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock = "Rock" + rock_pic
paper = "Paper" + paper_pic
scissors = "Scissors" + scissors_pic

moznosti = [rock, paper, scissors]

game = True

while game:
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    i = int(input("What do you choose? ")) - 1
    if (i == 0) or (i == 1) or (i == 2):
        my_choice = moznosti[i]
    else:
        print("Invalid choice. Choose again.")
        continue

    computer_choice = random.choice(moznosti)

    print(f"You choose: {my_choice}")
    print(f"Computer chooses: {computer_choice}")
  
    if (my_choice == moznosti[0] and computer_choice == moznosti[2]) or (my_choice == moznosti[1] and computer_choice == moznosti[0]) or (my_choice == moznosti[2] and computer_choice == moznosti[1]):
        print("You win!")
    elif my_choice == computer_choice:
        print("It's a draw!")
    else:
        print("You lost!")

    pokracovat = True
    while pokracovat:
        one_more = input("Do you want to play again? 'yes' or 'no' ")
        if one_more == "yes":
            pokracovat = False
        elif one_more == "no":
            pokracovat = False
            game = False
        else: 
            print("Invalid choice. Choose again.")
            continue

print("GG!\nThanks for playing.")