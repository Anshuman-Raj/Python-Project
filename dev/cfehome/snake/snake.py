from turtle import Turtle


class Snake:
    def __init__(self):
        self.body = []

        self.points = 0
        self.high_score = 0
        self.score = Turtle()
        self.score.color('green')
        self.score.pu()
        self.score.goto(0, 265)
        self.score.hideturtle()
        self.create()
        self.load_high_score()
        self.head = self.body[0]
        self.body_coordinates = [[x.xcor(), x.ycor()] for x in self.body[1:]]

    def create(self):
        for i in range(3):
            obj = Turtle(shape='square')
            obj.color('white')
            obj.pu()
            obj.goto(i * -20, 0)
            self.body.append(obj)

    def move(self):
        for segment in range(len(self.body) - 1, 0, -1):
            self.body[segment].goto(x=self.body[segment - 1].xcor(), y=self.body[segment - 1].ycor())
        # break
        self.body[0].forward(20)
        # sleep(0.1)

    def move_left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def move_right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

    def move_up(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def move_down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def eat(self):
        obj = Turtle(shape='square')
        obj.color('white')
        obj.pu()
        obj.goto(self.body[-1].xcor(), self.body[-1].ycor())
        self.body.append(obj)

        self.points += 1

    def body_check(self):
        self.body_coordinates = [[x.xcor(), x.ycor()] for x in self.body[1:]]
        if [self.body[0].xcor(), self.body[0].ycor()] in self.body_coordinates:
            return False
        else:
            return True

    # to give out coordinates of snake's head
    def x(self):
        return self.body[0].xcor()

    def y(self):
        return self.body[0].ycor()

    def update_score(self):
        self.score.clear()
        self.score.write(f"Score: {self.points}    High Score: {self.high_score}", align='center', font=('Arial', 24, 'normal'))

    def game_over(self):

        if self.points > self.high_score:
            self.high_score = self.points
            with open('highscore.txt', 'w') as highscore:
                highscore.write(str(self.high_score))

        self.score.goto(x=0, y=0)
        self.score.color('red')
        self.score.write("Game Over", align='center', font=('Arial', 24, 'normal'))

    def load_high_score(self):
        try:
            with open('highscore.txt', 'r') as highscore:
                self.high_score = int(highscore.read())
        except:
            pass
