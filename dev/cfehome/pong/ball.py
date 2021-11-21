from turtle import Turtle
from random import randint
import time


class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape('circle')
        self.headings = [randint(20, 70), randint(290, 340), randint(200, 250), randint(110, 160)]
        self.ball.color('white')
        self.ball.pu()
        self.ball.setheading(self.headings[randint(0, 3)])
        self.ball.goto(x=10, y=0)

    def move(self):
        self.ball.forward(25)
        time.sleep(0.01)

    def collide_with_paddle(self):
        angel_of_incidence = self.ball.heading()
        angle_of_reflection = (360 - angel_of_incidence + 180) % 360 + randint(-10, 10)
        self.ball.setheading(angle_of_reflection)

    def collide_with_wall(self):
        if self.ball.ycor() >= 270 or self.ball.ycor() <= -270:
            self.ball.setheading(360 - self.ball.heading())

        else:
            pass

    def keep_score(self, left, right):
        if self.ball.xcor() >= 280:
            left.update_score(up=1)
            self.ball.home()
            self.ball.setheading(self.headings[randint(0, 1)])
        elif self.ball.xcor() <= -290:
            right.update_score(up=1)
            self.ball.home()
            self.ball.setheading(self.headings[randint(2, 3)])
        else:
            pass
