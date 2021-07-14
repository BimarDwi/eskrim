
def board():
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


def letter():
    if letter_position.count("X") == letter_position.count("O"):
        return "X"
    else:
        return "O"


def player_move(n):
    print("It's " + str(n) + "'s turn")
    move = int(input("Choose your tile (1-9): "))
    letter_position[move] = n

    row = int((move - 1) / 3)
    column = int((move - 1) % 3)
    position[row][column] = n


def evaluation():
    # Check columns
    for row in position:
        if row[0] == row[1] and row[1] == row[2]:
            if row[0] == "X":
                return 1
            if row[0] == "O":
                return -1
    # Check row
    for row in position:
        if row == ["X", "X", "X"]:
            value = 1
            return value
        if row == ["O", "O", "O"]:
            value = -1
            return value
    # Check diagonal
    if position[0][0] == position[1][1] and position[1][1] == position[2][2]:
        if position[0][0] == "X":
            value = 1
            return value
        if position[0][0] == "O":
            value = -1
            return value
    if position[0][2] == position[1][1] and position[1][1] == position[2][0]:
        if position[0][2] == "X":
            value = 1
            return value
        if position[0][2] == "O":
            value = -1
            return value
    # Check draw
    if letter_position.count(" ") == 1:
        value = 0
        return value
    return None


def main():
    print(evaluation())
    while evaluation() is None:
        board()
        player_move(letter())
    if evaluation() == 1:
        board()
        print("Congrats! X wins!")
    if evaluation() == -1:
        board()
        print("Congrats! O wins!")
    if evaluation() == 0:
        board()
        print("It's a draw.")


while True:
    letter_position = [" " for x in range(10)]
    position = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    a = input("Do you want to play? y or n: ")
    if a == "y":
        main()
    else:
        break
