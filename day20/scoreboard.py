from turtle import Turtle

# Constants for scoreboard formatting
ALIGMENT = "center"
FONT = ("Courier", 24, "bold")
TEXT_COLOR = "white"

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(TEXT_COLOR)
        self.goto(0, 260)
        self.score = 0 # Set initial score to zero
        self.update_score()


    def update_score(self):
        """Updates the scoreboard with the current score"""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)


    def increase_score(self, count):
        """Increases the score by a given count and updates the scoreboard"""
        self.score += count
        self.update_score()


    def game_over(self):
        """Displays 'GAME OVER' message on the screen"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGMENT, font=FONT)
