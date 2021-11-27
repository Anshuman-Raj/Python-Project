from turtle import Turtle, Screen
from cars import Cars


def move():
    player.forward(20)
    # Function to move the turtle


def stop():
    pass
    # After hitting a car turtle does nothing


def score_update(score, cars):
    score.clear()
    score.write(f'Level: {cars.level}', font=('Arial', 20, 'bold'))
    # This function keeps the count of the score


# Description of the screen
screen = Screen()
screen.title('Turtle Crossing')
screen.bgcolor('yellow')
screen.setup(width=800, height=600)
screen.tracer(n=0)

# Level maintaining object
score_turtle = Turtle()
score_turtle.hideturtle()
score_turtle.pu()
score_turtle.color('blue')
score_turtle.goto(x=-360, y=270)

# Designing turtle for the player
player = Turtle(shape='turtle')
player.color('green')
player.pu()
player.goto(x=0, y=-280)
player.setheading(90)

# Getting the cars on the screen
game_cars = Cars()

# Updating the level
score_update(score_turtle, game_cars)
game_is_on = True

# Listening for 'Up' arrow key and updating the screen
screen.listen()
screen.update()
screen.onkeypress(key='Up', fun=move)

# try-except block in case user closes the window manually, no error should pop up
try:
    while game_is_on:

        game_cars.move()
        screen.update()
        if game_cars.distance(player) < 15:
            screen.onkeypress(key='Up', fun=stop)
            game_is_on = False
            score_turtle.goto(x=0, y=0)
            score_turtle.color('red')
            score_turtle.write('Game Over', align='center', font=('Arial', 24, 'normal'))

        if player.ycor() > 270:
            player.goto(x=0, y=-280)
            game_cars.level_up()
            score_update(score_turtle, game_cars)

    screen.mainloop()
except:
    pass
