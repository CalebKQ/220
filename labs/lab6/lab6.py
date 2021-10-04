"""
Name: Caleb Quattlebaum
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("What is your first and last name? ")
    split_list = name.split()
    print(split_list[1] + ", " + split_list[0])

def company_name():
    domain = input("What is your company's domain name? ")
    company = domain.split('.')
    print(company[1])

def initials():
    students = eval(input("How many students are in the class? "))
    for num in range(students):
        first = input("Enter the first name of student " + str(num + 1) + ": ")
        last = input("Enter " + first + "'s last name: ")
        name_initials = first[0] + last[0]
        print(first + "'s initials are " + name_initials + ".")

def names():
    all_names = input("Enters people's names, separated by commas: ")
    names = all_names.split(', ')
    print("The initials are", end=" ")
    for i in names:
        name = i.split()
        first = name[0]
        last = name[1]
        name_initials = first[0] + last[0]
        print(name_initials, end=" ")


def thirds():
    num = eval(input("How many sentences will there be? "))
    for i in range(num):
        sentence = input("Write sentence " + str(i + 1) + " here: ")
        for x in range(2, len(sentence), 3):
            print(sentence[x], end="")


def word_average():
    sentence = input("Write a sentence here: ")
    acc = 0
    sentence = sentence.split()
    for word in sentence:
        acc = acc + len(word)
    avg = acc / len(sentence)
    print(avg)

def pig_latin():
    sentence = input("Write a sentence here: ")
    sentence = sentence.lower()
    sentence = sentence.split()
    for word in sentence:
        print(word[1:] + word[0] + 'ay', end=' ')


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()
    # add other function calls here


main()
