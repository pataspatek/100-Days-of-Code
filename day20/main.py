from turtle import Turtle, Screen
from snake import Snake
import time


def main():
    screen = setup_screen()

    snake = Snake()

    setup_key_bindings(screen, snake)

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

    screen.exitonclick()


def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    return screen


def setup_key_bindings(screen, snake):
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


if __name__ == "__main__":
    main()
