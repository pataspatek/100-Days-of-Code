from turtle import Turtle, Screen
from random import randint


def main():
    tim = Turtle()
    screen = Screen()
    screen.colormode(255)

    for sites in range(3, 11):
        draw_shape(tim, sites)

    screen.exitonclick()


def draw_shape(turtle, sites):
    """Draws a shape with the given number of sides using the given turtle object."""
    turtle.color(random_color())

    for i in range(sites):
        turtle.forward(100)
        turtle.right(360 / sites)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


if __name__ == "__main__":
    main()