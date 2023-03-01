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
        self.score = 0 # Set initial score to zero
        self.before_game()
        

    def update_score(self):
        """Updates the scoreboard with the current score"""
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)


    def increase_score(self, count):
        """Increases the score by a given count and updates the scoreboard"""
        self.score += count
        self.update_score()


    def game_over(self):
        """Displays 'GAME OVER' message on the screen"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGMENT, font=FONT)


    def before_game(self):
        self.goto(0, 0)
        self.write("PRESS 'SPACE' TO START", align=ALIGMENT, font=FONT)
        self.goto(0, 260)
        self.write("SNAKE GAME!", align=ALIGMENT, font=FONT)
