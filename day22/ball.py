from turtle import Turtle
from random import randint

SHAPE = "circle"
COLOR = "white"


class Ball(Turtle):
    """A class to represent a ball in a Pong game."""

    def __init__(self):
        """Initialize a new Ball object."""
        super().__init__()

        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.movement = [randint(4, 7), randint(4, 7)]


    def move(self):
        """Move the ball by updating its position based on its movement vector."""
        new_x = self.xcor() + self.movement[0]
        new_y = self.ycor() + self.movement[1]
        self.goto(new_x, new_y)

    
    def bounce_x(self):
        self.movement[0] *= -1

    
    def bounce_y(self):
        self.movement[1] *= -1


    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

    

