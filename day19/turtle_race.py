from turtle import Turtle, Screen
from random import randint


SCREEN_WIIDTH = 500
SCREEN_HEIGHT = 450

TURTLES = ["red", "orange", "yellow", "green", "blue", "purple"]
ALL_TURTLES = []

FINISH_LINE = SCREEN_WIIDTH // 2 - 31


def main():
    # Set up the screen
    screen = Screen()
    screen.setup(SCREEN_WIIDTH, SCREEN_HEIGHT)
    screen.bgcolor("black")

    # Promt user for a bet
    user_bet = screen.textinput("Make your Bet!", "Which turtle will win the race?\nEnter a color: ")
    
    create_turtles()

    if user_bet:
        race_on = True
    
    while race_on:
        for turtle in ALL_TURTLES:
            turtle.forward(randint(1, 10))
            
            # Check if the turtle has crossed the finish line
            if turtle.xcor() > FINISH_LINE:
                winner = turtle.pencolor()

                if winner == user_bet:
                    print(f"You've won! The {winner} turtle is the winner!")
                else:
                    print(f"Sorry, you lost! The {winner} turtle is the winner!")

                race_on = False

    screen.exitonclick()


def create_turtles():
    '''Place turtles on the starting position'''
    x = -230
    y = -150

    for turtle_index in range(len(TURTLES)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(TURTLES[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=x, y=y)
        y += 60
        ALL_TURTLES.append(new_turtle)


if __name__ == "__main__":
    main()