"""
Name: Caleb Quattlebaum
lab1.py

Problem: This function calculates the area of a rectangle
"""

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

def shooting_percentage():
    total = eval(input("Enter total shots taken: "))
    made = eval(input("Enter total shots made"))
    percentage = made / total *100
    print("Shooting Percentage =", percentage)

def coffee():
    weight = eval(input("How much coffee was purchased in pounds? "))
    total = 10.50 * weight + 0.86 * weight + 1.50
    print("Total cost: $", total)

def kilometers_to_miles():
    kilo = eval(input("How many kilometers have you traveled? "))
    miles = kilo / 1.61
    print("You have traveled", miles, "miles")