from turtle import Screen, Turtle
import numpy as np

timmy = Turtle()

my_screen = Screen()
my_screen.colormode(255) 
timmy.shape('arrow')
timmy.speed(0)
# my_screen.tracer(0)
ymax = 240
ymin = -240
xmax = 240
xmin = -240

for y in range(ymin,ymax,20):
    for x in range(xmin,xmax,20):
        timmy.pencolor((np.random.randint(low=0,high=256), 
                        np.random.randint(low=0,high=256), 
                        np.random.randint(low=0,high=256)))
        timmy.penup()
        timmy.goto(x,y)
        timmy.dot(10)
timmy.hideturtle()


my_screen.exitonclick()

   