import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Turtle Game")
screen.tracer(0)

player = Player()
car_man = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_man.create_car()
    car_man.move_cars()

    for car in car_man.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_man.level_up()
        scoreboard.increase_level()

screen.exitonclick()