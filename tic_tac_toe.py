def board(position):
    print(f"   |   |   ")
    print(" " + position[0][0] + " | " + position[0][1] + " | " + position[0][2] + " ")
    print(f"   |   |   ")
    print("___________")
    print(f"   |   |   ")
    print(" " + position[1][0] + " | " + position[1][1] + " | " + position[1][2] + " ")
    print(f"   |   |   ")
    print("___________")
    print(f"   |   |   ")
    print(" " + position[2][0] + " | " + position[2][1] + " | " + position[2][2] + " ")
    print(f"   |   |   ")


def letter(curr_position):
    if sum(i.count("X") for i in curr_position) == sum(i.count("O") for i in curr_position):
        return "X"
    else:
        return "O"


def player_move(n, position):
    print("It's " + str(n) + "'s turn")
    move = int(input("Choose your tile (1-9): "))

    row = int((move - 1) / 3)
    column = int((move - 1) % 3)
    if position[row][column] == " ":
        position[row][column] = n
    else:
        board(position)
        print("The cell has been occupied, please choose another cell.")
        print("   ")
        player_move(n, position)


def computer_move(n, position, move):
    position[move[0]][move[1]] = n


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


def minimax(board, depth, isMax):
    score = evaluation(board)
    if score == 1:
        return score
    if score == -1:
        return score
    if score == 0:
        return score
    if isMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = " "
        return best

    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = " "
        return best


def finding_best_move(board):
    if letter(board) == "X":
        bes_val = -1000
        best_move = [-1, -1]
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    move_val = minimax(board, 0, False)
                    board[i][j] = " "
                    if move_val > bes_val:
                        best_move = [i, j]
                        bes_val = move_val
        return best_move
    if letter(board) == "O":
        bes_val = 1000
        best_move = [-1, -1]
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    move_val = minimax(board, 0, True)
                    board[i][j] = " "
                    if move_val < bes_val:
                        best_move = [i, j]
                        bes_val = move_val
        return best_move


def choose_player(game_mode):
    if game_mode == 1:
        player = input("p1 as X or p2 as O, p1 or p2?")
        if player == "p1":
            return "O"
        else:
            return "X"
    if game_mode == 2:
        player = input("p1 as X or p2 as O, p1 or p2?")
        if player == "p1":
            return "O"
        else:
            return "X"


def main():
    while True:
        position = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        play_status = input("Do you want to play? y or n: ")
        if play_status == "y":
            game_mode = int(input("Choose game mode:\n(1) Human vs Human\n(2) Human vs AI\nanswer:"))
            if game_mode == 1:
                board(position)
                while evaluation(position) is None:
                    turn = letter(position)
                    player_move(turn, position)
                    board(position)
                    if evaluation(position) == 1:
                        board(position)
                        print("Congrats! X wins!")
                    if evaluation(position) == -1:
                        board(position)
                        print("Congrats! O wins!")
                    if evaluation(position) == 0:
                        board(position)
                        print("It's a draw.")
            elif game_mode == 2:
                computer = choose_player(game_mode)
                while evaluation(position) is None:
                    turn = letter(position)
                    if turn != computer:
                        board(position)
                        player_move(turn, position)
                    else:
                        com_move = finding_best_move(position)
                        computer_move(turn, position, com_move)
                    if evaluation(position) == 1:
                        board(position)
                        print("Congrats! X wins!")
                    if evaluation(position) == -1:
                        board(position)
                        print("Congrats! O wins!")
                    if evaluation(position) == 0:
                        board(position)
                        print("It's a draw.")
        else:
            break


main()
