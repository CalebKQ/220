"""
Name: Caleb Quattlebaum
hangman.py
"""

from random import *

def wordlist(file):
    this_file = open(file, 'r')
    words = this_file.read()
    word_list = words.split(', ')
    return word_list

def word_choice(word_list):
    return word_list[randint(0, (len(word_list) - 1))]

def progression(guess, progress, answer):
    acc = 0
    blanks_list = list(progress)
    for letter in answer:
        if guess == letter:
            blanks_list[acc] = guess
        acc = acc + 1
    progress = "".join(blanks_list)
    return progress

def check_incorrect(guess, answer):
    acc = 0
    for letter in answer:
        if guess == letter:
            acc = acc + 1
    return bool(acc > 0)

def check_repeat(guess, all_guesses):
    acc = 0
    for letter in all_guesses:
        if guess == letter:
            acc = acc + 1
    return bool(acc > 0)

def win(progress, answer):
    return bool(progress == answer)

def play():
    word_list = wordlist('wordlist.txt')
    answer = word_choice(word_list)
    progress = '_' * len(answer)
    incorrect_guesses = []
    all_guesses = []
    while (not (win(progress, answer))) or (len(incorrect_guesses) < 7):
        print(progress)
        guess = input("Choose a letter. Guesses already made: " + str(incorrect_guesses) + " ")
        if check_repeat(guess, all_guesses):
            print("Sorry, you have already guessed that letter, try again")
        elif check_incorrect(guess, answer):
            progress = progression(guess, progress, answer)
        else:
            print("Sorry, that letter is not in the answer")
            incorrect_guesses.append(guess)
        all_guesses.append(guess)
        if win(progress, answer):
            print(answer)
            print("Congratulations, you won!")
            break
        elif len(incorrect_guesses) >= 7:
            print("Sorry, you lose, the answer was " + answer)
            break

def main():
    play()


main()
