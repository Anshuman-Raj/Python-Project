from turtle import Turtle
from random import randint
from time import sleep


# creating class for the Cars on the screen
class Cars:
    def __init__(self):
        self.level = 0  # Level decides the speed of cars
        self.number_of_cars = randint(20, 25)
        self.cars = []
        self.create_cars()

    # Creating the cars
    def create_cars(self):
        for _ in range(self.number_of_cars):
            obj = Turtle(shape='square')
            obj.color('red')
            obj.ht()
            obj.pu()
            obj.goto(x=randint(-300, 350), y=randint(-250, 250))
            obj.setheading(180)
            obj.st()
            self.cars.append(obj)

    # Moving the cars
    def move(self):
        for car in self.cars:
            if car.xcor() > -380:
                car.forward(20)
            else:
                car.ht()  # Hide Turtle
                car_y = car.ycor()
                car.goto(x=380, y=car_y)
                car.st()  # Show turtle

        if self.level <= 10:
            sleep(0.2-self.level*0.02)

    # Providing minimum distance from any car
    def distance(self, obj):
        dist = []
        for car in self.cars:
            dist.append(car.distance(obj))
        return min(dist)

    # Updating the level of the game and increasing number and speed of cars
    def level_up(self):
        self.level += 1
        for _ in range(len(self.cars)):
            car = self.cars.pop()
            car.hideturtle()
            car.goto(x=400, y=300)
        self.number_of_cars = randint(20+(self.level//2)*3, 25+(self.level//2)*3)
        self.create_cars()
