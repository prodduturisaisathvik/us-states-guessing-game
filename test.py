from turtle import Turtle,Screen
import  pandas as pd

screen=Screen()
screen.screensize(600,600)
screen.bgcolor("white")
screen.title("U.S.states")
tim = Turtle()
image="blank_states_img.gif"
screen.addshape(image)
tim.shape(image)
screen.exitonclick()


file=pd.read_csv("50_states.csv")
length=len(file["x"])
s=0
while s<length:
    name=screen.textinput("state","enter the name of the state")
    for index,states in file.iterrows():
        if name==states["state"]:
            tom=Turtle()
            tom.color("black")
            tom.penup()
            a=states["x"]
            b=states["y"]
            tom.goto(a,b)
            tom.write(states["state"])
            s=s+1




screen.exitonclick()