from snake import Snake
from food import Food, ExtraFood
from window import Window
from scoreboard import Scoreboard
import time
import random


def main():
    # Create a window object
    screen = Window()

    # Create a snake object
    snake = Snake()

    # Create a food object and an extra food object
    food = Food()
    extra_food = ExtraFood()

    # Create a scoreboard object
    scoreboard = Scoreboard()

    # At how many points the extra food will despawin again (starting with 1 due to % operator)
    food_despawn = 1

    # At how many points the extra food will despawin again (starting at 10 so that is the first time the extra food spawns)
    food_spawn = 10

    # Set up key bindings for the snake movement
    setup_key_bindings(screen, snake)

    # Game loop
    game_on = True
    while game_on:
        # Update the screen
        screen.update_screen()

        # Add a delay to slow down the game
        time.sleep(0.05)

        # Move the snake
        snake.move()

        # Detect collision with a food
        if snake.head.distance(food) < 15:
            # Increase the score, refresh the food, and extend the snake
            scoreboard.increase_score(1)
            food.refresh()
            snake.extend(1)

            # First spawn of the extra food when 10 points
            if scoreboard.score >= food_spawn:
                extra_food.refresh()
                food_despawn = scoreboard.score + random.randint(2, 6)
                food_spawn = scoreboard.score + random.randint(6, 9) 

        # Detect collision with extra food
        if snake.head.distance(extra_food) < 15:
            # Increase the score, hide the extra food, and extend the snake by 2
            scoreboard.increase_score(3)
            extra_food.hide()
            snake.extend(2)

        # Hide the extra food after a certain amount of time
        if scoreboard.score == food_despawn:
            extra_food.hide()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 250 or snake.head.ycor() < -280:
            # End the game and display the game over message
            game_on = False
            scoreboard.game_over()

        # Detect collision with tail excluding the head
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                # End the game and display the game over message
                game_on = False
                scoreboard.game_over()

    # Close the window when the game is over
    screen.screen.exitonclick()


def setup_key_bindings(screen, snake):
    # Listen for keyboard input
    screen.listen()

    # Set up the arrow keys to control the snake movement
    screen.screen.onkey(snake.up, "w")
    screen.screen.onkey(snake.down, "s")
    screen.screen.onkey(snake.left, "a")
    screen.screen.onkey(snake.right, "d")


if __name__ == "__main__":
    main()
