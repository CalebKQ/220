"""
Name: Caleb Quattlebaum
three_door_game.py

Purpose: Create a game that randomly selects a secret door and upon choosing one of the doors,
         the door turns green if you win, and red if you loose

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint
from graphics import GraphWin, Rectangle, Point, Text
from button import Button

# create a function to check which door is the secret door
def check_door(secret_door, door):
    return secret_door == door

def main():
    # create the window and 3 doors and draw the doors
    win = GraphWin("Three Door Game", 800, 600)

    door1 = Button(Rectangle(Point(200, 150), Point(300, 400)), 'Door 1')
    door2 = Button(Rectangle(Point(350, 150), Point(450, 400)), 'Door 2')
    door3 = Button(Rectangle(Point(500, 150), Point(600, 400)), 'Door 3')

    door1.draw(win)
    door2.draw(win)
    door3.draw(win)

    # create 2 lines of text that tell you what the game is and to click a door
    intro = Text(Point(400, 50), 'One of these doors is the secret door')
    intro.draw(win)
    prompt = Text(Point(400, 550), 'Click a door to choose it')
    prompt.draw(win)

    # put the doors into a list and use randint to randomly select a door
    door_list = [door1, door2, door3]
    secret_door = door_list[randint(0, 2)]

    # use if/elif statements to determine which door has been clicked
    # use if/else statements and the check_door function to see if user wins
    click = win.getMouse()

    if door1.is_clicked(click):
        if check_door(secret_door, door1):
            door1.color_button('green')
            win_text = 'Congratulations, you won!'
        else:
            door1.color_button('red')
            win_text = 'Sorry, you lose'
    elif door2.is_clicked(click):
        if check_door(secret_door, door2):
            door2.color_button('green')
            win_text = 'Congratulations, you won!'
        else:
            door2.color_button('red')
            win_text = 'Sorry, you lose'
    elif door3.is_clicked(click):
        if check_door(secret_door, door2):
            door3.color_button('green')
            win_text = 'Congratulations, you won!'
        else:
            door3.color_button('red')
            win_text = 'Sorry, you lose'

    # remove initial texts and replace with conclusion and exit messages
    intro.undraw()
    prompt.undraw()

    win_message = Text(Point(400, 50), win_text)
    end_message = Text(Point(400, 550), 'Click to close')
    win_message.draw(win)
    end_message.draw(win)

    # click again to close
    win.getMouse()

if __name__ == '__main__':
    main()
