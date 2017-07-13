# Turtle Training - Snowflake, the turtle creates a snowflake
# CTI-110
# Sigrid Olive
# 6/21/2017

# turtle and window for drawing
import turtle
win = turtle.Screen()
t = turtle.Turtle()

# display options
t.pensize(4)
t.pencolor("blue")
t.shape("turtle")

# draw polygon
numSides = 10
angle = 360 / numSides
sides = range(numSides)
distance = 80
increment = 10

# create polygon
for i in sides:
    t.forward(distance)
    t.left(angle)
t.left(90)
t.forward(10)
