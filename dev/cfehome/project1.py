from turtle import Turtle, Screen

from random import random, randint, uniform
turtle_obj = Turtle()
turtle_obj.shape("arrow")
turtle_obj.color('blue')
# turtle_obj.shapesize(2, 2, 2)
# dict = {0: 'blue', 1: 'white'}
# colormode(255)
# turtle_obj.pensize(5)

turtle_obj.speed('fastest')


def draw_shape(obj, num):

    angle = 360/num
    # color(random(),random(),random())
    for _ in range(num):
        obj.forward(100)
        obj.right(angle)


# for sides in range(3,11):
#     turtle_obj.color(random(),random(),random())
#     draw_shape(turtle_obj,sides)
# turtle_obj.color('blue')
def walk(obj):
    dict = {0: obj.right, 1: obj.left}
    dict_ang = {0: 0, 1: 90, 2: 180}
    obj.pensize(5)
    for i in range(randint(100, 300)):
        obj.color(random(), random(), random())
        obj.forward(25)
        dict[randint(0, 1325) % 2](dict_ang[randint(0, 7865) % 3])


def spirograph(obj):
    tilt = uniform(5,10)
    iterations = int(360/tilt+1)
    for iteration in range(iterations):
        obj.circle(100)
        obj.color(random(), random(), random())
        obj.right(tilt)


def draw_painting(obj):
    x, y = -400, -300
    obj.hideturtle()
    obj.pu()
    obj.pensize(10)
    for i in range(16):
        # obj.pu()
        obj.goto(x, y)
        for j in range(13):
            # obj.pd()
            obj.color(random(), random(), random())
            obj.dot()
            x += 60
            # obj.pu()
            obj.goto(x, y)
        y += 40
        x = -400


draw_painting(turtle_obj)
# spirograph(turtle_obj)
# walk(turtle_obj)

screen = Screen()
screen.exitonclick()
