from turtle import Turtle,Screen
import  pandas as pd
from scoreboard import Scoreboard



screen=Screen()
screen.screensize(600,600)
screen.setup(width=1.0, height=1.0)
screen.bgcolor("white")
screen.title("U.S.states")
tim = Turtle()
image="blank_states_img.gif"
screen.addshape(image)
tim.shape(image)
screen.tracer(0)
score_1 = Scoreboard()

score_1.chances()
file=pd.read_csv("50_states.csv")
length=len(file["x"])
s=0


while s<length:
    name=screen.textinput("state","enter the name of the state")
    if name is None:
        screen.exitonclick()
    l=length
    for index,states in file.iterrows():
        if name==states["state"].lower() :
            tom=Turtle()
            tom.color("black")
            tom.hideturtle()
            tom.penup()
            a=states["x"]
            b=states["y"]
            tom.goto(a,b)
            tom.write(states["state"])
            break

        else:
            l=l-1
    if l==0:
        score_1.update_scoreboard()
        screen.update()
    s=s+1




screen.exitonclick()