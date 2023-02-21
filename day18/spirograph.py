from turtle import Turtle, Screen
from random import randint


CIRCLE_NUMBER = 100


def main():
    turtle = Turtle()
    turtle.speed(0)
    turtle.hideturtle()

    screen = Screen()
    screen.colormode(255)

    for i in range(CIRCLE_NUMBER):
        draw_circle(turtle)
    
    screen.exitonclick()


def draw_circle(turtle):
    turtle.penup()
    turtle.pencolor(random_color())
    turtle.circle(100)
    turtle.right(360 / CIRCLE_NUMBER)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


if __name__ == "__main__":
    main()
