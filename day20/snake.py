from turtle import Turtle

SEGMENT_SIZE = 20
STARTING_POSITIONS = [(0, 0), (-1 * SEGMENT_SIZE, 0), (-2 * SEGMENT_SIZE, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():


    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]
        

    def create(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            new_segment.shapesize(SEGMENT_SIZE / 20, SEGMENT_SIZE / 20)
            self.segments.append(new_segment)


    def move(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_index - 1].xcor()
            new_y = self.segments[segment_index - 1].ycor()
            self.segments[segment_index].goto(new_x, new_y)

        self.head.forward(SEGMENT_SIZE)

    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
