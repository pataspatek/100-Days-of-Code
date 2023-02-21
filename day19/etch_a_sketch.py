from turtle import Turtle, Screen


def main():
    turtle = Turtle()
    screen = Screen()

    # Bind keys to functions
    screen.onkeypress(lambda: move_forward(turtle), "w")
    screen.onkeypress(lambda: move_backward(turtle), "s")
    screen.onkeypress(lambda: turn_left(turtle), "a")
    screen.onkeypress(lambda: turn_right(turtle), "d")
    screen.onkeypress(lambda: clear_screen(turtle), "c")

    # Set up the screen and listen for events
    screen.listen()
    screen.mainloop()


def move_forward(turtle):
    """Move the turtle forward."""
    turtle.forward(10)


def move_backward(turtle):
    """Move the turtle backward."""
    turtle.backward(10)


def turn_left(turtle):
    """Turn the turtle to the left."""
    turtle.left(10)


def turn_right(turtle):
    """Turn the turtle to the right."""
    turtle.right(10)


def clear_screen(turtle):
    """Clear the screen and return the turtle to its home position."""
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


if __name__ == "__main__":
    main()
