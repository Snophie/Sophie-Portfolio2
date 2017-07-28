
from turtle import *
import math


# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
userSquare= input("What color would you like your square to be? ")
userTriangle= input("What color would you like your triangle to be? ")
#x_pos = -250
#y_pos = -150
#t.setposition(x_pos, y_pos)

### Write your code below:
#code for the square
t.pencolor(userSquare)
t.pendown()
for x in range(0,4):
    t.forward(130)
    t.right(90)
t.penup()

#code for the triangle
x_pos = -250
y_pos = 300
t.setposition(x_pos, y_pos)
t.pencolor(userTriangle)
t.pendown()
for x in range(0,3):
    t.forward(130)
    t.right(120)






# Close window on click.
exitonclick()
