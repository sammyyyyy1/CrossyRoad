from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 5
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset()
        self.movements = []

    def at_finish(self):
        return self.ycor() >= FINISH_LINE_Y

    def reset(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def move_left(self):
        self.goto(x=self.xcor() - MOVE_DISTANCE, y=self.ycor())

    def move_right(self):
        self.goto(x=self.xcor() + MOVE_DISTANCE, y=self.ycor())

    def move(self):
        for movement in self.movements:
            movement()

    def stop_up_movement(self):
        if self.movements.count(self.move_up) > 0:
            self.movements.remove(self.move_up)

    def stop_down_movement(self):
        if self.movements.count(self.move_down) > 0:
            self.movements.remove(self.move_down)

    def stop_left_movement(self):
        if self.movements.count(self.move_left) > 0:
            self.movements.remove(self.move_left)

    def stop_right_movement(self):
        if self.movements.count(self.move_right) > 0:
            self.movements.remove(self.move_right)

    def add_up_movement(self):
        if self.movements.count(self.move_up) == 0:
            self.movements.append(self.move_up)
        self.stop_down_movement()

    def add_down_movement(self):
        if self.movements.count(self.move_down) == 0:
            self.movements.append(self.move_down)
        self.stop_up_movement()

    def add_left_movement(self):
        if self.movements.count(self.move_left) == 0:
            self.movements.append(self.move_left)
        self.stop_right_movement()

    def add_right_movement(self):
        if self.movements.count(self.move_right) == 0:
            self.movements.append(self.move_right)
        self.stop_left_movement()


