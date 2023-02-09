print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
names = name1 + name2

true_score = 0
love_score = 0

for name in names:
    for letter in name:
        if letter == "t" or letter == "r" or letter == "u" or letter == "e":
            true_score += 1
        if letter == "l" or letter == "o" or letter == "v" or letter == "e":
            love_score += 1
    
final_score = int(str(true_score) + str(love_score))

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")

elif final_score > 40 and final_score < 50:
    print(f"Your score is {final_score}, you are alright together.")
    
else:
    print(f"Your score is {final_score}.")