# Turtle Training (Shapes) - A turtle draws a square and a triangle
# CTI110
# 6/20/2017
# Sigrid Olive

import turtle #allows us to use turtles
win = turtle.Screen() #create a playground for turtles
t = turtle.Turtle()

#add some display options
t.pensize(3)  #increase pensize (takes integer)
t.pencolor("green") #set paint color
t.shape("turtle")
t.speed(2)

# commands from here to the last line can be replaced
# SQUARE
for size in range (4):
    side_length = 180;
    t.forward(175)
    t.left(90)

t.right(180) # turns around to start the triangle

# TRIANGLE
for size in range (3):
    side_length = 180
    t.forward(200)
    t.right(120)
    

