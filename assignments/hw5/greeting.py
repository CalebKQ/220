"""
Name: Caleb Quattlebaum
greeting.py

Purpose: create a Valentine's Day graphics card with a heart that gets an arrow
         shot through it

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import time

from graphics import GraphWin, Text, Point, Line, Circle, Polygon

def main():
    # create window, text, arrow, and heart objects
    win = GraphWin("Happy Valentine's Day!", 700, 500)
    message = Text(Point(350, 60), "Happy Valentine's Day!")
    # use a line with arrow head for the arrow
    # after finding a good endpoint position for the arrow, calc the slope
    # and move arrow off screen to move into position with loop animation
    arrow = Line(Point(-260, 575), Point(-15, 445))
    # make the heart from two circles and two triangles
    left_circle = Circle(Point(305, 225), 50)
    right_circle = Circle(Point(395, 225), 50)
    left_triangle = Polygon(Point(350, 225), Point(350, 355), Point(261, 249))
    right_triangle = Polygon(Point(350, 225), Point(350, 355), Point(439, 249))

    # draw all objects and adjust color, size, and style as needed for added flair
    win.setBackground("pink")

    message.draw(win)
    message.setFill("red")
    message.setSize(35)

    left_circle.draw(win)
    left_circle.setFill("red")
    left_circle.setOutline("red")
    left_circle.move(0, -10)

    left_triangle.draw(win)
    left_triangle.setFill("red")
    left_triangle.setOutline("red")
    left_triangle.move(0, -10)

    # position arrow between left and right side of the heart so
    # it looks like it is piercing the heart
    arrow.draw(win)
    arrow.setArrow("last")
    arrow.setWidth(7)
    arrow.setFill("purple")

    # add fletchings to the arrow to improve overall look
    fletch1 = Line(Point(-275, 565), Point(-250.2, 569.8))
    fletch1.draw(win)
    fletch1.setWidth(5)
    fletch1.setFill("purple")

    fletch2 = Line(Point(-260, 592), Point(-250.2, 569.8))
    fletch2.draw(win)
    fletch2.setWidth(5)
    fletch2.setFill("purple")

    fletch3 = fletch1.clone()
    fletch3.move((4.9 * 2), -(2.6 * 2))
    fletch3.draw(win)

    fletch4 = fletch2.clone()
    fletch4.move((4.9 * 2), -(2.6 * 2))
    fletch4.draw(win)

    fletch5 = fletch1.clone()
    fletch5.move((4.9 * 4), -(2.6 * 4))
    fletch5.draw(win)

    fletch6 = fletch2.clone()
    fletch6.move((4.9 * 4), -(2.6 * 4))
    fletch6.draw(win)

    right_circle.draw(win)
    right_circle.setFill("red")
    right_circle.setOutline("red")
    right_circle.move(0, -10)

    right_triangle.draw(win)
    right_triangle.setFill("red")
    right_triangle.setOutline("red")
    right_triangle.move(0, -10)

    # use small movements and large range to smooth out the movement
    # move with the original slope calculated for arrow
    for _ in range(51):
        x_movement = 0
        y_movement = 0
        time.sleep(0.0001)
        arrow.move(x_movement + (4.9 * 2), y_movement - (2.6 * 2))
        fletch1.move(x_movement + (4.9 * 2), y_movement - (2.6 * 2))
        fletch2.move(x_movement + (4.9 * 2), y_movement - (2.6 * 2))
        fletch3.move(x_movement + (4.9 * 2), y_movement - (2.6 * 2))
        fletch4.move(x_movement + (4.9 * 2), y_movement - (2.6 * 2))
        fletch5.move(x_movement + (4.9 * 2), y_movement - (2.6 * 2))
        fletch6.move(x_movement + (4.9 * 2), y_movement - (2.6 * 2))

    # add exit message telling user to click anywhere to close the window
    exit_message = Text(Point(350, 475), "Click anywhere to close")
    exit_message.draw(win)

    # use getMouse to wait for the user to click the window to close
    win.getMouse()


if __name__ == "__main__":
    main()
