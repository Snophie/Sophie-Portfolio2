
from turtle import *
import math


# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.

color= input("What color would you like your shape to be? ")
sides= input("How many sides does your shape have? ")
length= input("How long do you want your sides to be? ")
xcor= input("Where do you want your x coordinate to be? ")
ycor= input("Where do you want your y coordinate to be? ")
setup(float(xcor), float(ycor))
### Write your code below:
#code for the square
t.pencolor(color)
t.pendown()
for x in range(0,int(sides)):
    t.forward(float(length))
    t.right(360/int(sides))


# Close window on click.
exitonclick()
