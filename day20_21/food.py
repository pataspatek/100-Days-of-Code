from turtle import Turtle
from random import randint

from snake import SEGMENT_SIZE


class Food(Turtle):
    """
    A class to represent the food that the snake can eat.
    Inherits from the Turtle class.
    """


    def __init__(self):
        """
        Initializes a new Food object with a circle shape and blue color.
        The food is placed in a random position on the screen.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5 * (SEGMENT_SIZE / 20), 0.5 * (SEGMENT_SIZE / 20))
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        """
        Moves the food to a new random position on the screen.
        """
        random_x = randint(-260, 260)
        random_y = randint(-230, 230)
        self.goto(random_x, random_y)


class ExtraFood(Food):
    """
    A class to represent the extra food that gives the player extra points.
    Inherits from the Food class.
    """

    def __init__(self):
        """
        Initializes a new ExtraFood object with a yellow color and larger size than regular food.
        The extra food is initially hidden from the screen.
        """
        super().__init__()
        self.color("yellow")
        self.shapesize(1, 1)
        self.hide()


    def hide(self):
        """
        Moves the extra food to a position outside of the screen to hide it.
        """
        self.goto(-500, -500)
