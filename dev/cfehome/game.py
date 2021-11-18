from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food

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
while game_is_on:
    if food.x()-20 <= snake.x() <= food.x()+20:
        if food.y()-20 <= snake.y() <= food.y()+20:
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


    if snake.body[0].xcor() >= 280 or snake.body[0].xcor() <= -280 or snake.body[0].ycor() >= 280 or snake.body[
        0].ycor() <= -280:
        game_is_on = False
    sleep(0.1)
screen.mainloop()
