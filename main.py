import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

level = 1
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.add_up_movement, "Up")
screen.onkeypress(player.add_down_movement, "Down")
screen.onkeypress(player.add_left_movement, "Left")
screen.onkeypress(player.add_right_movement, "Right")
screen.onkeyrelease(player.stop_up_movement, "Up")
screen.onkeyrelease(player.stop_down_movement, "Down")
screen.onkeyrelease(player.stop_left_movement, "Left")
screen.onkeyrelease(player.stop_right_movement, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    player.move()
    car_manager.create_car()
    car_manager.move_cars()

    # check player collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # check successful cross
    if player.at_finish():
        car_manager.next_level()
        player.reset()
        scoreboard.next_level()


screen.exitonclick()