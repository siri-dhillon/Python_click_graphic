# Created by Sirpreet Kaur Dhillon 
# on June 29th 2022 

# Program: 
# Inputs the number of shapes from the user 
# Generates a window on screen to input mouse clicks 
# Draws 1/4 shapes (square, circle, dot, or line) using graphics.py
# based on the region of the screen the user clicks on
# Screen is divided into 4 quadrants:
## Top Right : Square
## Bottom Right : Line
## Top Left : Circle
## Bottom Left : Dots

import random
from graphics import * 

# user input
maximumPoints = int(input("Enter number of shapes: "))

def main(): 
    # Graphics Window
    win = GraphWin("click Fun", 500, 500)
    for i in range(maximumPoints): 

        # Mouse Click input
        p = win.getMouse()

        # Getting the X and Y values of the mouse click
        x = p.getX()
        y = p.getY()

        # Printing the x and y coordinates in terminal
        print("Point " + str(i) +": (" + str(x) + ", " + str(y) + ")")

        # Creating all variables needed to create the shapes 
        point1 = Point(x, y)
        radius = random.randrange(0,50)
        outline_color = color_rgb(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        fill_color = color_rgb(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        
        # Dividing the screen into 4 parts to print 4 different shapes
        if (x < 250 and y > 250):
            # Prints a point in the bottom left region
            point1.draw(win)
        elif(x < 250 and y < 250): 
            # Prints a circle in the top left region
            circle = Circle(point1, radius)
            circle.setOutline(outline_color)
            circle.setFill(fill_color)
            circle.draw(win)
        elif(x > 250 and y > 250):
            
            # select direction of line
            sel = random.randrange(0,20)
            if(sel < 5):
                point2 = Point(x + radius, y + radius)
            elif(sel < 10):
                point2 = Point(x + radius, y - radius)
            if(sel < 15):
                point2 = Point(x - radius, y + radius)
            else: 
                point2 = Point(x - radius, y - radius)

            # Used to generate line
            line = Line(point1, point2)
            line.draw(win)
        else: 
            # Generates a square of diagonal = radius 
            square = Rectangle(point1, Point(x-radius, y-radius))
            square.setOutline(outline_color)
            square.setFill(fill_color)
            square.draw(win)
main()