#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Title: SPACE ZOOM BACKGROUND
Author: Vikki Wong
Edited by: Rishi Assar
September 16, 2020
Revised Date: October 4, 2020

A turtle art piece that is comprised of a planetary scene, 
one main planet in the upper left with a elliptical ring, 
a gif background with many stars,  as well as many turtle 
drawn diamonds and stars throughout the window.

Criticism Sandwich:
    
 1. The quality of the code is stellar for the amount we 
 learned about code organization and comments at the time.
 
 2. There are some areas where the final image could have
 been improved as well as some collsollidation using for loops.
 Also the code can be improved by creating more turtles.
 I thought it would be cool to randomize the location of the stars
 as in real space the stars do not follow any spacial patters. 
 
 
 3. I really liked the final design image the turtle created.
 The gif background as well as the varience in types of stars, 
 their locations, and the colors were all on point. 
 
 Artistic Feedback:
     
     I really liked the color choice for the planet, stars, and background.
     The contrast between the two star colors added a nice depth to the image.
     
'''

from turtle import * #import the library of commands that you'd like to use
from math import *
import random
colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 550 # changed width of panel to match the size of the gif
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

image = "aADEYCh.gif" # starry night sky background gif imported, make sure in same file location as .py file
panel.bgcolor("black") # sets background color to black
panel.bgpic(image) # sets background pic to gif 

#=======Add your code here======

#creates turtles
purplePlanet = Turtle() # creates turtle for planet
planetRing = Turtle() # creates turtle for planet ring
pentagramStar = Turtle() # creates turtle for larger 5 point yellow starts
octagramStar = Turtle()  # creates turtle for snaller 8 point lighter starts
asteroidShape = Turtle()  # creates turtle for diamond asteroid shape

#first planet

purplePlanet.speed(0) # speed of planet turtle
purplePlanet.goto(-150, 240) # location of planet  
purplePlanet.color("violet") # color of planet turtle
purplePlanet.down() # pen down
purplePlanet.begin_fill() # fill planet with same color 
purplePlanet.circle(-70) # radius of planet
purplePlanet.end_fill() # end fill after shape is drawn
purplePlanet.up() # pen up
purplePlanet.color(208,110,228) # secondary color on planet

purplePlanet.goto(-199,216) # location of first detailed line on planet
purplePlanet.down() # pen down
purplePlanet.width(8) # width of first curved line
purplePlanet.circle(150,27) # portion of circle drawn on planet
purplePlanet.up() # pen up

purplePlanet.goto(-207,139) # second detailed line on planet
purplePlanet.seth(0) # changes orientation of turtle to an angle
purplePlanet.width(10) # changes width of second line
purplePlanet.down() # pen down
purplePlanet.circle(250,29) # portion of circle drawn 
purplePlanet.up() # pen up

purplePlanet.goto(-180, 107) # location of third line
purplePlanet.seth(0) # changes orientation of turtle to an angle
purplePlanet.down() # pen down
purplePlanet.width(3) # changes width of thrid line
purplePlanet.circle(200,24) # portion of circle drawn
purplePlanet.up() # pen up

purplePlanet.goto(-120,200) # location of dot detail
purplePlanet.dot(30) # dot radius
purplePlanet.up() # pen up
purplePlanet.seth(0) # changes orientation of turtle to an angle

#planetary ring parametric ellipse

planetRing.up() # pen up
planetRing.speed(0) # speed of planet ring turtle, could not get this going faster for some reason
planetRing.color("white") # color of turtle
planetRing.width(2) # width of turtle

for angle in range(37,335): # this loop creates an ellipse for the planetary ring
    angle=radians(angle) # iterates through range to determine angle of line
    x=130*(sin(angle)) # x value 130 times sin of the iterated angle
    y=30*(cos(angle)) # y value 30 times cos of the iterated angle
    planetRing.goto(x-160,y+165) # go to function changes as x and y are resassigned due to loop
    planetRing.down() # pen down

#pentagram nested loops

pentagramStar.speed(0) # pentagram star turtle speed
pentagramStar.width(3) # pentagram star turtle width
        
for i in range(8): # creates loop that randomizes the location of 8 five point stars
    pentagramStar.up() # pen up
    pentagramStar.goto(random.randint(-180,200),random.randint(-70,180)) #randomizes the location of the stars within certain limits
    pentagramStar.down() # pen down
    for i in range(5): # draws 5 lines which comprise the star
        pentagramStar.color("yellow") # color of lines
        pentagramStar.forward(45) # length of each line
        pentagramStar.right(144) # angle of rotation to draw the stars

#octagram nested loops 

octagramStar.speed(0) # octagram star turtle speed
octagramStar.width(2) # octagram star turtle width

for i in range(10): # creates loop that randomizes the location of 10 eight point stars
    octagramStar.up() # pen up
    octagramStar.goto(random.randint(-103,200),random.randint(-143,290)) #randomizes the location of the stars within certain limits
    octagramStar.down() # pen down
    for i in range(8): # draws 8 lines which comprise the star
        octagramStar.color(252,250,182) # color of lines
        octagramStar.forward(20) # length of each line
        octagramStar.right(135) # angle of rotation to draw the stars
 
#parametric asteroid

asteroidShape.up() # pen up
asteroidShape.width(3) # asteroid star turtle width
asteroidShape.speed(0) # asteroid star turtle speed
asteroidShape.color(245,201,120) # asteroid star turtle color

for angle in range(360): # creates loop that creates 4 curved lines that connect to make a diamond
    #for i in [10,20,30]:
        angle=radians(angle) # determines angle in radians using range(360)
        x=80*(cos(angle))**3 # x value 80 times cos of the iterated angle to the third power
        y=80*(sin(angle))**3 # y value 80 times sin of the iterated angle to the third power
        asteroidShape.goto(x-120,y-230) # location of the asteroid using previous x and y values 
        asteroidShape.down() # pen down

#hide turtles

purplePlanet.ht()
planetRing.ht()
pentagramStar.ht()
octagramStar.ht()
asteroidShape.ht()






