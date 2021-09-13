"""
Name: Caleb Quattlebaum
lab3.py

Problem: lab 3 programs
"""

import math

def average():
    assignments = eval(input("How many assignments have been graded? "))
    acc = 0
    for i in range(1, assignments + 1):
        grade = eval(input("Enter HW" + str(i) + " grade: "))
        acc = grade + acc
    final = acc / assignments
    print("Your overall grade is:", final)

def tip_jar():
    acc = 0
    for i in range(5):
        tip = eval(input("How much would you like to tip? "))
        acc = acc + tip
    total = acc
    print("Total tips collected: $", round(total, 2))

def newton():
    x = eval(input("Approximate the square root of: "))
    approx = x / 2
    for i in range(10):
        sqroot = (approx + (x / approx)) / 2
    print("The square root of " + str(x) + " is approximately: ", sqroot)

def sequence():
    terms = eval(input("How many numbers are in this sequence? "))
    for i in range(1, terms):
        sequence = 1 + i // 2 *2
        print(sequence)

def pi():
    n = eval(input("How many terms are in this series? "))
    acc = 1
    for x in range(n):
        num = 2 + (x // 2 * 2)
        den = 1 + ((x + 1) // 2 * 2)
        frac = num / den
        acc = acc * frac
    print(acc)
