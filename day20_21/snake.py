from turtle import Turtle

# Set the size of each segment of the snake
SEGMENT_SIZE = 15

# Set the starting positions for the snake's segments
STARTING_POSITIONS = [(0, 0), (-1 * SEGMENT_SIZE, 0), (-2 * SEGMENT_SIZE, 0)]

# Set the headings for each direction
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("cornflower blue")
        

    def create_snake(self):
        """Creates the snake by adding segments to the starting positions"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        """Adds a new segment to the snake"""
        new_segment = Turtle("square")

        # Alternate the colors of the segments
        if len(self.segments) % 2 == 0:
            new_segment.color("dark gray")
        else:
            new_segment.color("white smoke")

        # Set the position and size of the new segment
        new_segment.penup()
        new_segment.goto(position)
        new_segment.shapesize(SEGMENT_SIZE / 20, SEGMENT_SIZE / 20)

        # Add the new segment to the list of segments
        self.segments.append(new_segment)

    
    def extend(self, count):
        """Adds multiple segments to the snake"""
        for i in range(count):
            self.add_segment(self.segments[-1].position())


    def move(self):
        """Moves the snake forward one segment at a time"""
        # Move each segment to the position of the segment in front of it
        for segment_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_index - 1].xcor()
            new_y = self.segments[segment_index - 1].ycor()
            self.segments[segment_index].goto(new_x, new_y)

        # Move the head segment forward one segment size
        self.head.forward(SEGMENT_SIZE)

    
    def up(self):
        """Changes the direction of the snake to up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        """Changes the direction of the snake to down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        """Changes the direction of the snake to left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        """Changes the direction of the snake to right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
