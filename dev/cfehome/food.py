from turtle import Turtle
from random import randint


class Food:
    def __init__(self):
        self.obj = Turtle()
        self.obj.color('blue')
        self.obj.hideturtle()
        self.obj.pu()
        self.obj.shape('circle')


    def add_food(self):
        self.obj.clear()
        self.obj.goto(x=randint(-275, 275), y=randint(-275, 275))
        self.obj.dot()

    def x(self):
        return self.obj.xcor()

    def y(self):
        return self.obj.ycor()


