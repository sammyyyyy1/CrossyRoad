import random
from turtle import Turtle, TurtleScreen

STARTING_MOVE_DISTANCE = 3
STARTING_FREQUENCY = 10
CAR_IMAGES = ["blue_car.png", "brown_car.png", "green_car.png", "grey_car.png",
              "orange_car.png", "pink_car.png", "purple_car.png",
              "red_car.png", "yellow_car.png"]
COLOURS = ["red", "blue", "pink", "purple", "orange", "green", "brown", "grey", "yellow"]

class CarManager:

    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.frequency = STARTING_FREQUENCY
        self.all_cars = []

    def create_car(self):
        car_spawn = random.randint(0, self.frequency)
        if car_spawn == 0:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLOURS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)
            if car.xcor() < -280:
                car.reset()
                car.hideturtle()
                self.all_cars.remove(car)

    def next_level(self):
        if self.speed < 13:
            self.speed += 0.5
        if self.speed % 1 == 0 and self.frequency > 1:
            self.frequency -= 1

