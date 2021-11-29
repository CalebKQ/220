"""
Name: Caleb Quattlebaum
lab13.py
"""

from graphics import *

def is_in_binary_search(search_val, values):
    left = 0
    right = len(values) - 1
    while left <= right:
        middle = (left + right) // 2
        middle_value = values[middle]
        if search_val == middle_value:
            return True
        if search_val < middle_value:
            right = middle - 1
        if search_val > middle_value:
            left = middle + 1
    return False

def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        position = i
        for j in range(i + 1, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                position = j
        values[i], values[position] = values[position], values[i]
    return values

def calc_area(rectangle):
    point1 = rectangle.getP1()
    point2 = rectangle.getP2()
    dx = abs(point1.getX() - point2.getX())
    dy = abs(point1.getY() - point2.getY())
    return dx * dy

def rect_sort(rectangles):
    dict = {}
    areas = []
    for rect in rectangles:
        dict[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = dict[(areas[i])]
    return rectangles

def star_find(filename):
    file = open(filename, 'r')
    signals = file.read().split()
    found = []
    acc = 0
    for i in range(len(signals)):
        if 4000 <= int(signals[i]) <= 5000:
            found.append(signals[i])
        if len(found) >= 5:
            break
        acc += 1
    print(len(found), " values were found.")
    if len(found) >= 5:
        print("Here is what was found:", found)
        print(acc + 1, "signals were searched before finding the fifth signal")
    else:
        print("We did not find the neutron star.")

def main():
    print(is_in_binary_search(23, [1, 4, 16, 20, 23, 35]))  # should return True
    print(is_in_binary_search(24, [1, 4, 16, 20, 23, 35]))  # should return False
    print(selection_sort([2, 3, 5, 1, 4]))  # should print the sorted list
    r1 = Rectangle(Point(0, 5), Point(3, 10))
    r2 = Rectangle(Point(0, 5), Point(2, 8))
    r3 = Rectangle(Point(0, 5), Point(4, 12))
    print(rect_sort([r1, r2, r3]))  # should print the rectangles sorted by area
    star_find("signals.txt")

main()
