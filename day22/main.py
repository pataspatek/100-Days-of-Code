from window import Window
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def main():
    window = Window()
    scoreboard = Scoreboard()

    right_paddle = Paddle((350, 0), ("Up", "Down"))
    left_paddle = Paddle((-350, 0), ("w", "s"))
    window.key_listener(right_paddle)
    window.key_listener(left_paddle)

    ball = Ball()

    game_on = True
    while game_on:
        time.sleep(0.03)
        window.screen.update()
        
        ball.move()

        # Detect collision with a wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with a paddle
        if ball.distance(right_paddle) < 50 and ball.xcor() > 335 or ball.distance(left_paddle) < 50 and ball.xcor() < -335:
            ball.bounce_x()

        # Right missed
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.left_point()

        # Left missed
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.right_point()

    # Exit on click 
    window.screen.exitonclick()




if __name__ == "__main__":
    main()