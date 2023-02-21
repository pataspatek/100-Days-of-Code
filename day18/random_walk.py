from turtle import Turtle, Screen
from random import randint, choice


DIRECTIONS = [0, 90, 180, 270]
MOVE_DISTANCE = 30


def main():
    turtle = Turtle()
    turtle.speed(0)
    turtle.pensize(10)
    turtle.hideturtle()

    screen = Screen()
    screen.colormode(255)

    for _ in range(200):
        move(turtle)

    screen.exitonclick()


def move(turtle):
    """Moves the turtle in a random direction and color."""
    turtle.pencolor(random_color())
    turtle.forward(MOVE_DISTANCE)
    turtle.setheading(choice(DIRECTIONS))


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


if __name__ == "__main__":
    main()
