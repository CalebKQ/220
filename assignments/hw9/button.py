"""
Name: Caleb Quattlebaum
button.py

Purpose: Create a class to make a button to use in other programs

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Text

class Button:
    """
    Creates a clickable button from a Rectangle object and a string.
    With methods to get the string that appears on the button,
    draw and undraw the button in the window, check if the button
    has been clicked, and set a new string that will appear on
    the button.
    """
    # requires Rectangle object and a string
    def __init__(self, rectangle, label):
        self.shape = rectangle
        self.center = rectangle.getCenter()
        self.point1 = rectangle.getP1()
        self.point2 = rectangle.getP2()
        self.text = Text(self.center, label)
        self.label = label

    # returns string that appears on the button
    def get_label(self):
        return self.label

    # draws the button in the window
    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    # removes the button from the window
    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    # checks to see if the button has been clicked
    def is_clicked(self, point):
        return (self.point1.getX() <= point.getX() <= self.point2.getX() and
                self.point1.getY() <= point.getY() <= self.point2.getY())

    # change the background color of the button
    def color_button(self, color):
        self.shape.setFill(color)

    # set a new string to appear on the button
    def set_label(self, label):
        self.text = Text(self.center, label)
