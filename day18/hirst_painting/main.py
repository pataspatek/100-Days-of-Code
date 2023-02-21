from turtle import Turtle, Screen
from random import choice

# A list of colors to choose from
COLORS = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

# The size of each dot
DOT_SIZE = 20

# The distance to move between each dot
MOVE = 70

# The number of dots in each row and column
DOT_NUMBER = 10

# The starting position of the dots
STARTING_POSITION = -300


def main():
    # Create a turtle object
    turtle = Turtle()
    turtle.penup()
    turtle.speed(0)
    turtle.hideturtle()
    
    # Set the color mode of the screen
    screen = Screen()
    screen.colormode(255)

    for row in range(DOT_NUMBER):
        # Move the turtle to the starting position of the row
        new_row(turtle, row)

        # Draw the dots for the current row
        for col in range(DOT_NUMBER):
            draw_dot(turtle, choice(COLORS))
        

    screen.exitonclick()


def draw_dot(turtle, color):
    """Draw a dot with the given color and size."""
    turtle.dot(DOT_SIZE, color)
    turtle.forward(MOVE)
    

def new_row(turtle, row):
    """Move the turtle to the starting position of the given row."""
    turtle.goto(STARTING_POSITION, STARTING_POSITION + (MOVE * row))


if __name__ == "__main__":
    main()
