"""
Name: Caleb Quattlebaum
lab9.py
"""
import math

from graphics import *

def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10
    print(nums)

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])

def writeSumOfSquares():
    input_file = input('What is your input filename? ')
    output_file = input('What is your output filename? ')
    infile = open(input_file, 'r')
    outfile = open(output_file, 'w')
    for line in infile:
        nums = line.split()
        toNumbers(nums)
        squareEach(nums)
        summation = sumList(nums)
    outfile.write('Sum of Squares = ' + str(summation))
    infile.close()
    outfile.close()

def starter():
    weight = eval(input("What is the player's weight? "))
    numWins = eval(input("How many wins does the player have? "))
    if 150 <= weight < 160 and numWins >= 5:
        print("this player can be a starter")
    elif weight > 199 or numWins > 20:
        print("this player can be a starter")
    else:
        print("this player cannot be a starter")

def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(str(year) + " is a leap year")
    else:
        print(str(year) + " is not a leap year")

def circleOverlap():
    win = GraphWin("Overlap Circles", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    c1 = Circle(p1, r)
    c1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    c2 = Circle(p3, r2)
    c2.draw(win)

    distance = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)

    if distance <= r + r2:
        overlap = Text(Point(200, 25), "The circles overlap")
        overlap.draw(win)
    else:
        not_overlap = Text(Point(200, 25), "The circles do not overlap")
        not_overlap.draw(win)

    close_message = Text(Point(200, 375), "Click anywhere to close")
    close_message.draw(win)

    win.getMouse()
    win.close()

def main():
    addTen([5, 2, -3])
    writeSumOfSquares()
    starter()
    leapYear(2000)
    leapYear(2100)
    circleOverlap()

main()
