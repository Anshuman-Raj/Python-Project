from turtle import Turtle, Screen
from random import randint

# turtle_obj = Turtle()
# turtle_obj.color('red')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
obj_list = []
is_race_on = False
# def move_forward():
#     turtle_obj.forward(10)
#
#
# def move_backward():
#     turtle_obj.backward(10)
#
#
# def move_clockwise():
#     turtle_obj.right(10)
#
#
# def move_counter_clockwise():
#     turtle_obj.left(10)
#
#
# def clear():
#     turtle_obj.clear()
#     turtle_obj.pu()
#     turtle_obj.home()
#     turtle_obj.pd()


screen = Screen()
screen.setup(width=500, height=400)
screen.listen()
for i in range(7):
    obj_list.append(Turtle(shape='turtle'))
    obj_list[i].color(colors[i])
    obj_list[i].pu()
    obj_list[i].goto(-240, -150+50*i)

color_bet = screen.textinput(title="Choose your turtle", prompt="Please enter the color of the ture you are betting on: ")
if color_bet in colors:
    is_race_on = True
else:
    print("This color is not available")

while is_race_on:

    for turtle in obj_list:
        if turtle.xcor() > 230:
            is_race_on = False

            if turtle.pencolor() == color_bet:
                print("Congrats! Your turtle has won the race!")
            else:
                print("Sorry, %s colored turtle has won the race." % turtle.pencolor())
            break
        random_distance = randint(0, 11)
        turtle.forward(random_distance)


# screen.onkeypress(key="w", fun=move_forward)
# screen.onkeypress(key="s", fun=move_backward)
# screen.onkeypress(key="a", fun=move_clockwise)
# screen.onkeypress(key="d", fun=move_counter_clockwise)
# screen.onkeypress(key="c", fun=clear)


screen.exitonclick()
