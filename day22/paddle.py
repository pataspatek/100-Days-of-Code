from turtle import Turtle

COLOR = "white"
SHAPE = "square"

UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self, position, keys):
        super().__init__()

        '''Initialize a new paddle object'''

        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.goto(position)
        self.shapesize(5, 1)
        self.keys = (keys)
        self.move_step = 20

    
    def up(self):
        new_y = self.ycor() + self.move_step
        self.goto(self.xcor(), new_y)

    
    def down(self):
        new_y = self.ycor() - self.move_step
        self.goto(self.xcor(), new_y)