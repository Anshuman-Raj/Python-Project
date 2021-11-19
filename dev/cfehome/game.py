from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from tkinter import Tk, Label

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(n=0)
screen.bgcolor('black')
screen.title('Snake Game')
snake = Snake()
food = Food()
food.add_food()
screen.listen()
game_is_on = True
snake.update_score()
while game_is_on:
    if snake.head.distance(food.obj) < 15:
        snake.eat()
        food.add_food()
        snake.update_score()
        # print(food.x(), snake.x())
    screen.update()
    snake.move()
    game_is_on = snake.body_check()
    screen.onkeypress(key="Up", fun=snake.move_up)
    screen.onkeypress(key="Down", fun=snake.move_down)
    screen.onkeypress(key="Left", fun=snake.move_left)
    screen.onkeypress(key="Right", fun=snake.move_right)

    if snake.body[0].xcor() >= 280 or snake.body[0].xcor() <= -280 or snake.body[0].ycor() >= 280 or \
            snake.body[0].ycor() <= -280:
        game_is_on = False

    sleep(0.15)
snake.game_over()

screen.mainloop()
