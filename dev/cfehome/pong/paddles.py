from turtle import Turtle


class Paddle:
    def __init__(self, side='left'):
        """
        The Paddle class will put the functioning paddles on the screen
        side: choose whether the paddle this is being created will be on left side or right
        control: To choose whether the paddle will be controlled by arrow keys or with 'W' and 'S'
        """
        self.paddle_list = []
        self.side = side
        self.dict = {'left': -1, 'right': 1}
        self.color_dict = {'left': 'blue', 'right': 'red'}
        self.score = 0
        self.score_writer = Turtle()
        self.score_writer.hideturtle()
        self.score_writer.color(self.color_dict[self.side])
        self.score_writer.pu()
        self.create_paddle()

    def create_paddle(self):
        if self.side == 'left':
            t = -10
        else:
            t = 0
        for i in range(5):
            obj = Turtle(shape='square')
            obj.hideturtle()
            obj.color('white')
            obj.pu()
            obj.goto(x=self.dict[self.side]*280+t, y=40-i*20)
            obj.setheading(90)
            obj.showturtle()
            self.paddle_list.append(obj)

    def move_up(self):
        if self.paddle_list[0].ycor() < 280:
            for obj in self.paddle_list:
                obj.forward(40)
            # time.sleep(0.1)

    def move_down(self):
        if self.paddle_list[-1].ycor() > -280:
            for obj in self.paddle_list:
                obj.backward(40)
            # time.sleep(0.1)

    def distance(self, turtle_object):
        distance_list = []
        for obj in self.paddle_list:
            distance_list.append(obj.distance(turtle_object))
        return min(distance_list)

    def update_score(self, up=0):
        self.score += up
        self.score_writer.goto(x=self.dict[self.side]*70, y=250)
        self.score_writer.clear()
        self.score_writer.write(f'{self.score}', font=('Arial', 36, 'bold'))
