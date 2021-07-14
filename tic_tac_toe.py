def board(letter_position):
    print(f"   |   |   ")
    print(" " + letter_position[1] + " | " + letter_position[2] + " | " + letter_position[3] + " ")
    print(f"   |   |   ")
    print("___________")
    print(f"   |   |   ")
    print(" " + letter_position[4] + " | " + letter_position[5] + " | " + letter_position[6] + " ")
    print(f"   |   |   ")
    print("___________")
    print(f"   |   |   ")
    print(" " + letter_position[7] + " | " + letter_position[8] + " | " + letter_position[9] + " ")
    print(f"   |   |   ")


def letter(letter_position):
    if letter_position.count("X") == letter_position.count("O"):
        return "X"
    else:
        return "O"


def player_move(n, letter_position, position):
    print("It's " + str(n) + "'s turn")
    move = int(input("Choose your tile (1-9): "))
    letter_position[move] = n

    row = int((move - 1) / 3)
    column = int((move - 1) % 3)
    position[row][column] = n


def evaluation(curr_position):
    # Check columns
    for i in range(3):
        if curr_position[0][i] == curr_position[1][i] and curr_position[1][i] == curr_position[2][i]:
            if curr_position[0][i] == "X":
                return 1
            if curr_position[0][i] == "O":
                return -1
    # Check row
    for row in curr_position:
        if row == ["X", "X", "X"]:
            value = 1
            return value
        if row == ["O", "O", "O"]:
            value = -1
            return value
    # Check diagonal
    if curr_position[0][0] == curr_position[1][1] and curr_position[1][1] == curr_position[2][2]:
        if curr_position[0][0] == "X":
            value = 1
            return value
        if curr_position[0][0] == "O":
            value = -1
            return value
    if curr_position[0][2] == curr_position[1][1] and curr_position[1][1] == curr_position[2][0]:
        if curr_position[0][2] == "X":
            value = 1
            return value
        if curr_position[0][2] == "O":
            value = -1
            return value
    # Check draw
    if sum(i.count(" ") for i in curr_position) == 0:
        value = 0
        return value
    return None


def main():
    while True:
        letter_position = []
        for x in range(10):
            letter_position.append(" ")
        position = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        a = input("Do you want to play? y or n: ")
        if a == "y":
            while evaluation(position) is None:
                board(letter_position)
                player_move(letter(letter_position), letter_position, position)
            if evaluation(position) == 1:
                board(letter_position)
                print("Congrats! X wins!")
            if evaluation(position) == -1:
                board(letter_position)
                print("Congrats! O wins!")
            if evaluation(position) == 0:
                board(letter_position)
                print("It's a draw.")
        else:
            break
