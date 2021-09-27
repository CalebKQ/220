"""
Name: Caleb Quattlebaum
lab5.py
"""
import math

from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)
    text_start = Point(win_width / 2, win_height - 30)
    message = Text(text_start, "Click to close the window")

    # Add code here to get the dimensions and draw the target
    rad = 250 / 5
    center = Point(250, 250)
    yellow_circle = Circle(center, rad)
    yellow_circle.setFill('yellow')

    red_circle = Circle(center, rad * 2)
    red_circle.setFill('red')

    blue_circle = Circle(center, rad * 3)
    blue_circle.setFill('blue')

    black_circle = Circle(center, rad * 4)
    black_circle.setFill('black')

    white_circle = Circle(center, rad * 5)
    white_circle.setFill('white')

    white_circle.draw(win)
    black_circle.draw(win)
    blue_circle.draw(win)
    red_circle.draw(win)
    yellow_circle.draw(win)
    message.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    click1 = win.getMouse()
    click1.draw(win)
    click2 = win.getMouse()
    click2.draw(win)
    click3 = win.getMouse()
    click3.draw(win)

    tri = Polygon(click1, click2, click3)
    tri.draw(win)

    # and display its area in the graphics window.
    c1x = click1.getX()
    c1y = click1.getY()
    c2x = click2.getX()
    c2y = click2.getY()
    c3x = click3.getX()
    c3y = click3.getY()

    dx1 = c2x - c1x
    dy1 = c2y - c1y
    dx2 = c3x - c2x
    dy2 = c3y - c2y
    dx3 = c1x - c3x
    dy3 = c1y - c3y

    a = math.sqrt(dx1 ** 2 + dy1 ** 2)
    b = math.sqrt(dx2 ** 2 + dy2 ** 2)
    c = math.sqrt(dx3 ** 2 + dy3 ** 2)

    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    perimeter_txt = Text(Point(win_width / 2, win_height - 40), "The perimeter is: " + str(perimeter))
    perimeter_txt.draw(win)
    area_txt = Text(Point(win_width / 2, win_height - 15), "The area is: " + str(area))
    area_txt.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    red_input = Entry(Point(win_width / 2, win_height / 2 + 40), 3)
    red_input.draw(win)
    red_val = 255

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    green_input = Entry(Point(win_width / 2, win_height / 2 + 70), 3)
    green_input.draw(win)
    green_val = 255

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    blue_input = Entry(Point(win_width / 2, win_height / 2 + 100), 3)
    blue_input.draw(win)
    blue_val = 255

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        win.getMouse()

        red_val_txt = red_input.getText()
        red_val = int(red_val_txt)
        green_val_txt = green_input.getText()
        green_val = int(green_val_txt)
        blue_val_txt = blue_input.getText()
        blue_val = int(blue_val_txt)
        
        color = color_rgb(red_val, green_val, blue_val)

        shape.setFill(color)


    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    user_input = input("Write a message here: ")
    print(user_input[0])
    print(user_input[-1])
    print(user_input[2:6])
    print(user_input[0] + user_input[-1])
    print(user_input[:3] * 10)
    for i in user_input:
        print(i)
    print(len(user_input))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[2] + values[0] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    num = eval(input("How many terms are in this series? "))
    acc = 0
    for i in range(num):
        series = 2 + (2 * (i % 3))
        print(series, end=" ")
        acc = acc + series
    print("")
    print("sum = ", acc)


def main():
    target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()
    pass


main()
