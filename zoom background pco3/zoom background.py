#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Title: SPACE ZOOM BACKGROUND
Author: Vikki Wong
September 16, 2020
'''

from turtle import * #import the library of commands that you'd like to use
from math import *
colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

image = "aADEYCh.gif" #starry night sky background
panel.bgcolor("black")
panel.bgpic(image)

#=======Add your code here======

#this resets everything before drawing
ht()
shape("classic")
shapesize(1,1,1)
speed(0)
clear()
home()
up()
width(1)

#first planet
goto(-150, 240)
color("violet")
down()
begin_fill()
circle(-70)
end_fill()
up()
color(208,110,228)

goto(-199,216)
down()
width(8)
circle(150,27)
up()

goto(-207,139)
seth(0)
width(10)
down()
circle(250,29)
up()

goto(-180, 107)
seth(0)
down()
width(3)
circle(200,24)
up()

goto(-120,200)
dot(30)
up()
seth(0)


#planetary ring parametric ellipse

color("white")
width(2)

for angle in range(37,335):
    angle=radians(angle)
    x=130*(sin(angle))
    y=30*(cos(angle))
    goto(x-160,y+165)
    down()

width(3)

#pentagram nested loops
for i in [(130,180),(5,35),(150,-70),(5,270),(60, -197),(-180,-25) ]:
    up()
    goto(i)
    down()
    for i in range(5):
        color("yellow")
        forward(45)
        right(144)

width(2)

#octagram nested loops 
for i in [(85,152),(-23,-17),(117,-92),(-37,213),(12, -143),(-103,-83),(202,47),(188,290)]:
    up()
    goto(i)
    down()
    for i in range(8):
        color(252,250,182)
        forward(20)
        right(135)
 
up()
color(245,201,120)

#parametric asteroid
for angle in range(360):
    #for i in [10,20,30]:
        angle=radians(angle)
        x=80*(cos(angle))**3
        y=80*(sin(angle))**3
        goto(x-120,y-230)
        down()


#part of reset sequence
up()







