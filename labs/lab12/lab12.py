"""
Name: Caleb Quattlebaum
lab12.py
"""

from random import randint

def find_and_remove_first(my_list, value):
    try:
        i = my_list.index(value)
        my_list[i] = "Caleb Quattlebaum"
    except:
        pass

def read_data(filename):
    file = open(filename, 'r')
    data = file.read()
    data = data.split()
    return data

def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val in values:
            return True
        i += 1
    return False

def good_input():
    x = eval(input("Enter a number: "))
    while x < 1 or x > 10:
        x = eval(input("Enter a number: "))
    return x

def num_digits():
    x = eval(input("Enter a positive number: "))
    while x >= 1:
        digits = 1
        while x // 10 != 0:
            x //= 10
            digits += 1
        print(digits)
        x = eval(input("Enter a positive number: "))

def hi_lo_game():
    secret = randint(1, 100)
    guess = 0
    num = eval(input("Guess the number: "))
    while num != secret and guess < 7:
        guess += 1
        if num > secret:
            print("Guess was too high")
        else:
            print("Guess was too low")
        num = eval(input("Guess another number: "))
    if num == secret:
        print("Correct, you win in", guess, "guesses!")
    else:
        print("Sorry, you lose! The number was", secret)


def main():
    find_and_remove_first([1, 2, 3, 4, 5, 6], 3)
    read_data("values.txt")
    is_in_linear(3, read_data("values.txt"))
    good_input()
    num_digits()
    hi_lo_game()

main()
