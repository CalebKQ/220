"""
Name: Caleb Quattlebaum
lab10.py
"""

def build_board():
    positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return positions

def display_board(positions):
    counter = 0
    print("-" * 13)
    for i in range(3):
        print("| ", end="")
        for j in range(3):
            print(positions[counter], end=" | ")
            counter = counter + 1
        print("\n" + "-" * 13)

def place_spot(positions, spot, marker):
    positions[spot - 1] = marker

def legal_spot(positions, spot):
    if (positions[spot - 1] == "X" or positions[spot - 1] == "O") or (spot < 1 or spot > 9):
        return False
    else:
        return True

def game_won(positions):
    win_con = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for condition in win_con:
        x_counter = 0
        o_counter = 0
        for spot in condition:
            if positions[spot - 1] == "X":
                x_counter = x_counter + 1
            elif positions[spot - 1] == "O":
                o_counter = o_counter + 1
        if x_counter == 3:
            return "X wins"
        elif o_counter == 3:
            return "O wins"

def game_over(positions, turn_count):
    if (game_won(positions) == "X wins" or game_won(positions) == "O wins") or (turn_count > 8):
        return True
    else:
        return False

def play_game():
    positions = build_board()
    display_board(positions)
    turn_count = 0
    while not(game_over(positions, turn_count)):
        spot = eval(input("X's turn "))
        if legal_spot(positions, spot):
            place_spot(positions, spot, "X")
        display_board(positions)
        if game_won(positions):
            print(game_won(positions))
        turn_count = turn_count + 1
        spot = eval(input("O's turn "))
        if legal_spot(positions, spot):
            place_spot(positions, spot, "O")
        display_board(positions)
        if game_won(positions):
            print(game_won(positions))
        turn_count = turn_count + 1


def main():
    play_game()


main()
