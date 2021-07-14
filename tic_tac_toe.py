
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


def game_status():
    # Check columns
    for i in position:
        if i[0] == i[1] and i[1] == i[2]:
            return 1
    # Check row
    for i in range(3):
        if position[0][i] == position[1][i] and position[1][i] == position[2][i]:
            return 1
    # Check diagonal
    if position[0][0] == position[1][1] and position[1][1] == position[2][2]:
        return 1
    if position[0][2] == position[1][1] and position[1][1] == position[2][0]:
        return 1
    # Check draw
    if letter_position.count(" ") == 1:
        return 0
    return -1


def main():
    board()
    player_move(letter())
    if game_status() == -1:
        return main()
    if game_status() == 1:
        board()
        if letter() == "O":
            winner = "X"
        else:
            winner = "O"
        print("Congrats! " + winner + " wins!")
    if game_status() == 0:
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
