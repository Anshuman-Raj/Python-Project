from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
from time import sleep
screen = Screen()
screen.setup(width=600, height=600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(n=0)
draw_screen = Turtle()
draw_screen.hideturtle()
draw_screen.color('white')
draw_screen.pu()
draw_screen.goto(x=10, y=-290)
draw_screen.pd()
draw_screen.setheading(90)
for _ in range(15):
    draw_screen.forward(20)
    draw_screen.pu()
    draw_screen.forward(20)
    draw_screen.pd()

paddle_right = Paddle(side='right')
paddle_left = Paddle(side='left')
paddle_left.update_score()
paddle_right.update_score()
ball = Ball()
screen.listen()
while paddle_left.score < 5 and paddle_right.score < 5:
    ball.move()
    sleep(0.10)
    screen.onkeypress(key="Up", fun=paddle_right.move_up)
    screen.onkeyrelease(key='Up', fun=None)
    screen.onkeypress(key="Down", fun=paddle_right.move_down)
    screen.onkeyrelease(key='Down', fun=None)
    screen.onkeypress(key="w", fun=paddle_left.move_up)
    screen.onkeyrelease(key='w', fun=None)
    screen.onkeypress(key="s", fun=paddle_left.move_down)
    screen.onkeyrelease(key='s', fun=None)
    if paddle_left.distance(ball.ball) <= 20:
        ball.collide_with_paddle()
    if paddle_right.distance(ball.ball) <= 20:
        ball.collide_with_paddle()
    sleep(0.02)
    ball.collide_with_wall()
    ball.keep_score(paddle_left, paddle_right)
    screen.update()

draw_screen.pu()
draw_screen.goto(x=0, y=0)
if paddle_left.score == 5:
    draw_screen.color('blue')
    draw_screen.write('Blue Won', align='center', font=('Arial', 24, 'bold'))
else:
    draw_screen.color('red')
    draw_screen.write('Red Won', align='center', font=('Arial', 24, 'bold'))
screen.mainloop()
