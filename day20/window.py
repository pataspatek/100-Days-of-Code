from turtle import Screen, Turtle

# Set constants for the screen width and height
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Window():


    def __init__(self):
        # Create a new Screen object
        self.screen = Screen()
        
        # Set up the screen
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        
        # Turn off screen updates
        self.screen.tracer(0)

        # Draw the borders
        self.draw_borders()


    def update_screen(self):
        # Update the screen
        self.screen.update()


    def listen(self):
        # Tell the screen to listen for key presses
        self.screen.listen()


    def draw_borders(self):
        # Create a Turtle object for drawing the borders
        border_turtle = Turtle()
        border_turtle.speed(0)
        border_turtle.penup()
        border_turtle.hideturtle()
        border_turtle.goto(-298, -285)
        border_turtle.pensize(10)
        border_turtle.pendown()
        border_turtle.color("red")

        # Draw the four borders of the game area
        for i in range(4):
            if i % 2 == 0:
                border_turtle.forward(583)
                border_turtle.left(90)
            else:
                border_turtle.forward(538)
                border_turtle.left(90)
