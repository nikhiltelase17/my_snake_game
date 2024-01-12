from turtle import Screen
from snake import Snake
from score import Score
from food import Food
import time
import pygame

# SOUND EFFECTS
pygame.mixer.init()
background_sound = pygame.mixer.Sound("background_music.mp3")
eat_sound = pygame.mixer.Sound("eat_food.mp3")
game_over_sound = pygame.mixer.Sound("game_over.mp3")

# playing background sound
pygame.mixer.Sound.play(background_sound)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("------WELCOME TO SNAKE GAME------".center(130))
screen.tracer(0)

snake = Snake()
score = Score()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        pygame.mixer.Sound.play(eat_sound)

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()
        pygame.mixer.Sound.stop(background_sound)
        pygame.mixer.Sound.play(game_over_sound)

    # Detect collision with tail.
    # if head collides with any segment in the tail.
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
            pygame.mixer.Sound.stop(background_sound)
            pygame.mixer.Sound.play(game_over_sound)

screen.exitonclick()
