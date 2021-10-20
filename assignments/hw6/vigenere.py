"""
Name: Caleb Quattlebaum
vigenere.py

Purpose: create a GUI asks user for a message and a key then outputs a coded message using a Vigenere Cipher

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *

# create code(message, keyword) function
def code(message, keyword):
    # make a list of all caps alphabet to use for index later
    vig_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                   'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # capitalize user's message and remove spaces
    cap_message = message.upper()
    message_nospace = cap_message.replace(" ", "")
    cap_keyword = keyword.upper()
    keyword_nospace = cap_keyword.replace(" ", "")
    # create accumulator to store letters from for loop
    encoded_message = ""

    # create for loop to break message down and implement vigenere cipher for each letter
    # using the given key
    for letter in range(len(message_nospace)):
        # subtract 65 from ord() to map A = 0, B = 2, ... Z = 25
        num_message = ord(message_nospace[letter]) - 65
        # use if/else statements to ensure the key will continue to be used even after
        # the length of the message exceeds the length of the key
        if letter > (len(keyword_nospace) - 1):
            # use loop iteration mod length of the key to continue to cycle through the key
            num_key = ord(keyword_nospace[letter % len(keyword_nospace)]) - 65
        else:
            num_key = ord(keyword_nospace[letter]) - 65
        # add each key number to each message number
        new = (num_message + num_key)
        # use new number to index list of caps alphabet
        # use if/else statements for when new number exceeds the range of the list
        if new > 25:
            encoded_message = encoded_message + vig_letters[(new % 25) - 1]
        else:
            encoded_message = encoded_message + vig_letters[new]
    # return the encoded message
    return encoded_message

# create main() function to create GUI for program
def main():
    # create window, text, input boxes, and button for GUI
    win = GraphWin("Vigenere", 500, 300)

    message_text = Text(Point(90, 50), "Message to code:")
    message_text.draw(win)

    message_input = Entry(Point(315, 50), 32)
    message_input.draw(win)

    key_text = Text(Point(100, 100), "Enter Keyword:")
    key_text.draw(win)

    key_input = Entry(Point(261, 100), 20)
    key_input.draw(win)

    encode_text = Text(Point(250, 175), "Encode")
    button_outline = Rectangle(Point(200, 200), Point(300, 150))
    encode_text.draw(win)
    button_outline.draw(win)

    # get mouse for button click
    win.getMouse()

    # call previously created code() function using input from GUI as parameters
    encoded_message = code(message_input.getText(), key_input.getText())

    # undraw button and replace with encoded message
    encode_text.undraw()
    button_outline.undraw()

    new_text = Text(Point(250, 175), "Resulting Message:")
    new_message = Text(Point(250, 200), encoded_message)

    new_text.draw(win)
    new_message.draw(win)

    # add exit message that tells user to click anywhere to close
    exit_message = Text(Point(250, 275), "Click anywhere to close window")
    exit_message.draw(win)

    # get mouse to close
    win.getMouse()

# run program
if __name__ == "__main__":
    main()
