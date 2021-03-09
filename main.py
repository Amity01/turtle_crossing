import time,random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(player.move_forward, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.2)
    if random.randint(1, 3) == 1:
        car_manager.create_car()
    car_manager.move_cars()
    if player.ycor() > 280:
        scoreboard.update()
        car_manager.increase_speed()
        player.start()
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.gameover()
    screen.update()

screen.exitonclick()
