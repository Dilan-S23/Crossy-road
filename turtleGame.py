import time
from turtle import Screen,Turtle
from random import choice,randint


###################################
#car class
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.penup()
        self.a = randint(-240,240)
        self.color(choice(COLORS))
        self.goto(320,self.a)
        self.left(180)


#################################
#player class
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
    def go(self):
        self.forward(MOVE_DISTANCE)
    def level(self):
        self.goto(STARTING_POSITION)


##################################
#score class

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
    def leve(self):
        self.goto(-295,265)
        self.write(f"Level = {self.level}",False,"left",FONT)

    def over(self):
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write(f"Game over!!",False,"left",FONT)

##############################main
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


tt = Player()
score = Scoreboard()
ss = Scoreboard()
screen.onkey(fun=tt.go,key="Up")


game_is_on = True

car = []

def go():
    car.append(CarManager())
aa = 6
score.leve()
while game_is_on:
    time.sleep(0.1)

    if tt.ycor() == FINISH_LINE_Y:
        tt.level()
        score.clear()
        score.level +=1
        score.leve()

        MOVE_INCREMENT += 5


    for i in car:
        choice(car).forward(MOVE_INCREMENT)

        if tt.distance(i) <20:
            ss.over()
            screen.exitonclick()

    if aa % 6 ==0:
        go()
    aa +=1

    screen.update()

