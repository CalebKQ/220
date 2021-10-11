"""
Name: Caleb Quattlebaum
Partner: N/A
lab7.py
"""
import math

def cash_conversion():
    num = eval(input("Type in a number: "))
    print("${:.2f}".format(num))

def encode():
    x = input("what would you like to say? ")
    key = eval(input("what is the key? "))
    acc = ""
    for c in x:
        i = ord(c)
        new = chr(i + key)
        acc = acc + new
    print(acc)

def sphere_area(radius):
    surface_area = math.pi * (radius ** 2)
    return surface_area

def sphere_volume(radius):
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume

def sum_n(n):
    acc = 0
    for i in range(n + 1):
        acc = acc + i
    return acc

def sum_n_cubes(n):
    acc = 0
    for i in range(n + 1):
        acc = acc + (i ** 3)
    return acc

def encode_better():
    m = input("What would you like to say? ")
    n = input("What is your key? ")
    acc = ""
    for i in range(len(m)):
        c = ord(m[i])
        key = ord(n[i])
        new = (c + key) - 97
        acc = acc + chr(new)
    print(acc)

def main():
    cash_conversion()
    encode()
    print(sphere_area(2))
    print(sphere_volume(2))
    print(sum_n(5))
    print(sum_n_cubes(5))
    encode_better()

main()
