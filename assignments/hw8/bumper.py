"""
Name: Caleb Quattlebaum
bumper.py

Purpose: create a program that sends two circles bouncing in random directions
         where they can bounce off of the borders of the windows and bounce off
         of each other

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
import time
from random import randint
from graphics import GraphWin, Circle, Point, color_rgb

def get_random(move_amount):
    return randint(move_amount * -1, move_amount)

def did_collide(ball1, ball2):
    center1 = ball1.getCenter()
    center_x1 = center1.getX()
    center_y1 = center1.getY()
    rad1 = ball1.getRadius()

    center2 = ball2.getCenter()
    center_x2 = center2.getX()
    center_y2 = center2.getY()
    rad2 = ball2.getRadius()

    distance = math.sqrt((center_x2 - center_x1) ** 2 + (center_y2 - center_y1) ** 2)

    return bool(distance <= (rad1 + rad2))

def hit_vertical(ball, win):
    bottom_border = win.getHeight()
    rad = ball.getRadius()
    center = ball.getCenter()
    center_y = center.getY()
    top = center_y - rad
    bottom = center_y + rad

    return bool(top <= 0 or bottom >= bottom_border)

def hit_horizontal(ball, win):
    right_border = win.getWidth()
    rad = ball.getRadius()
    center = ball.getCenter()
    center_x = center.getX()
    left = center_x - rad
    right = center_x + rad

    return bool(left <= 0 or right >= right_border)

def get_random_color():
    color_r = randint(0, 255)
    color_g = randint(0, 255)
    color_b = randint(0, 255)

    return color_rgb(color_r, color_g, color_b)

def main():
    win = GraphWin("Bumper", 600, 400)
    ball1 = Circle(Point(125, 125), 30)
    ball2 = Circle(Point(375, 375), 30)

    ball1.draw(win)
    ball2.draw(win)

    win.setBackground(get_random_color())
    ball1.setFill(get_random_color())
    ball2.setFill(get_random_color())

    x1_move = get_random(10)
    y1_move = get_random(10)
    x2_move = get_random(10)
    y2_move = get_random(10)

    while x1_move < 11:
        top_left1 = ball1.getP1()
        top_left2 = ball2.getP1()
        top1 = top_left1.getY()
        top2 = top_left2.getY()
        left1 = top_left1.getX()
        left2 = top_left2.getX()

        time.sleep(0.0001)

        ball1.move(x1_move, y1_move)
        ball2.move(x2_move, y2_move)

        if did_collide(ball1, ball2):
            if top1 < top2 and left1 < left2:
                x1_move = randint(-10, -1)
                y1_move = randint(-10, -1)
                x2_move = randint(1, 10)
                y2_move = randint(1, 10)
            elif top1 < top2 and left1 > left2:
                x1_move = randint(1, 10)
                y1_move = randint(-10, -1)
                x2_move = randint(-10, -1)
                y2_move = randint(1, 10)
            elif top1 > top2 and left1 < left2:
                x1_move = randint(-10, -1)
                y1_move = randint(1, 10)
                x2_move = randint(1, 10)
                y2_move = randint(-10, -1)
            elif top1 > top2 and left1 > left2:
                x1_move = randint(1, 10)
                y1_move = randint(1, 10)
                x2_move = randint(-10, -1)
                y2_move = randint(-10, -1)
            else:
                x1_move = get_random(10)
                y1_move = get_random(10)
                x2_move = get_random(10)
                y2_move = get_random(10)

        if hit_horizontal(ball1, win):
            if left1 <= 0:
                x1_move = randint(1, 10)
            else:
                x1_move = randint(-10, -1)

        if hit_horizontal(ball2, win):
            if left2 <= 0:
                x2_move = randint(1, 10)
            else:
                x2_move = randint(-10, -1)

        if hit_vertical(ball1, win):
            if top1 <= 0:
                y1_move = randint(1, 10)
            else:
                y1_move = randint(-10, -1)

        if hit_vertical(ball2, win):
            if top2 <= 0:
                y2_move = randint(1, 10)
            else:
                y2_move = randint(-10, -1)


    win.getMouse()

if __name__ == "__main__":
    main()
