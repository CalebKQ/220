"""
Name: <Caleb Quattlebaum>
lab4.py
"""

from graphics import *
from math import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move circle")
    instructions.draw(win)

    # builds a circle
    #shape = Circle(Point(50, 50), 20)
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        acc = shape.clone()
        acc.draw(win)
        acc.move(dx, dy)
    closer = Text(inst_pt, "Click again to quit")
    instructions.undraw()
    closer.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """

    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)
    text_start = Point(width / 2, height - 10)
    message = Text(text_start, "Click two points on the screen")
    message.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()

    rec = Rectangle(p1, p2)
    rec.setFill("blue")
    rec.setOutline("yellow")
    rec.draw(win)

    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()

    perimeter = abs(x2 - x1) + abs(y2 - y1)
    area = abs(x2 - x1) * abs(y2 - y1)
    perimeter_txt_start = Point(width / 2, 15)
    perimeter_txt = Text(perimeter_txt_start, ("Perimeter: ", perimeter))
    area_txt_start = Point(width / 2, 35)
    area_txt = Text(area_txt_start, ("Area: ", area))
    perimeter_txt.draw(win)
    area_txt.draw(win)

    closer = Text(text_start, "Click again to quit")
    message.undraw()
    closer.draw(win)
    win.getMouse()
    win.close()

def circle():
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)
    text_start = Point(width / 2, height - 10)
    message = Text(text_start, "Click two points on the screen")
    message.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    x = x2 - x1
    y = y2 - y1

    radius = sqrt(x ** 2 + y ** 2)
    rad_text_start = Point(width / 2, 20)
    rad_text = Text(rad_text_start, ("Radius: ", radius))
    rad_text.draw(win)

    circ = Circle(p1, radius)
    circ.setFill("blue")
    circ.draw(win)


    closer = Text(text_start, "Click again to quit")
    message.undraw()
    closer.draw(win)
    win.getMouse()
    win.close()

def pi2():
    n = eval(input("How many terms are in this series? "))
    acc = 0
    for x in range(n):
        num = 4
        denom = 1 + 2 * x
        frac = (num / denom) * ((-1) ** x)
        acc = acc + frac

    print("Your number is: ", acc)
    print("Deviation from pi: ", pi - acc)

def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
