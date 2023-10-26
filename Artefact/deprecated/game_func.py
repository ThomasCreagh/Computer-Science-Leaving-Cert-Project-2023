# DO NOT RUN, OUTDATED CODE...

from random import randint as r_int

# Make this a class at some point


def display(board: list) -> None:
    # This part prints out each of the display number on the top
    print("\t", end="")
    for i in range(1, COLUMNS+1):
        print(i, end="\t")
    print("\n"*3)

    for i in range(ROWS):
        print(i+1, end="\t")
        for j in range(COLUMNS):
            if board[i][j] == 0:
                print(".", end="\t")
            elif board[i][j] == 1:
                print("X", end="\t")
            else:
                print("O", end="\t")
        print("\n"*3)
    print()


def check_columns(board: list) -> list:
    moves = [i for i in range(len(board[0])) if board[0][i] == 0]
    return moves


def move(board: list, column: int, player: int) -> list:
    new_board = board

    for i in range(ROWS-1, -1, -1):
        if new_board[i][column] == 0:
            new_board[i][column] = player
            break

    return new_board


def check_game(board: list) -> bool:
    # This is for horizontal checking
    for row in board:
        for col in range(len(board[0])-CONNECTED+1):
            if row[col] != 0:
                outcome = True
                for num_c in range(col, CONNECTED+col-1):
                    if row[num_c] != row[num_c+1]:
                        outcome = False
                if outcome:
                    return True

    # This is for verticaly checking
    for col in range(len(board[0])):
        for row in range(len(board)-CONNECTED+1):
            if board[row][col] != 0:
                outcome = True
                for num_r in range(row, CONNECTED+row-1):
                    if board[num_r][col] != board[num_r+1][col]:
                        outcome = False
                if outcome:
                    return True

    # This is for diagonaly checking
    for row in range(len(board)-CONNECTED+1):
        for col in range(len(board[0])-CONNECTED+1):
            if board[row][(len(board[0])-col)-1] != 0:
                outcome = True
                for num_r, num_c in zip(range(row, CONNECTED+row-1), range(col, CONNECTED+(len(board[0])-col)-2)):
                    if board[num_r][(len(board[0])-num_c)-1] != board[num_r+1][(len(board[0])-num_c)-2]:
                        outcome = False
                if outcome:
                    return True

            if board[row][col] != 0:
                outcome = True
                for num_r, num_c in zip(range(row, CONNECTED+row-1), range(col, CONNECTED+col-1)):
                    if board[num_r][num_c] != board[num_r+1][num_c+1]:
                        outcome = False
                if outcome:
                    return True

    for row in board:
        if 0 in row:
            return False

    return True


def ask_for_dimentions(var) -> int:
    if var == "ROWS":
        rows = input("Enter number of rows: ")
        if verify_int(rows):
            return rows
        else:
            return ask_for_dimentions("ROWS")

    elif var == "COLUMNS":
        columns = input("Enter number of columns: ")
        if verify_int(columns):
            return columns
        else:
            return ask_for_dimentions("COLUMNS")

    elif var == "CONNECTED":
        connected = input(
            "Enter number of symbols in a row nessasary to win: ")
        if verify_int(connected):
            return connected
        else:
            return ask_for_dimentions("CONNECTED")


def verify_int(_input):
    try:
        _ = int(_input)
        return True
    except:
        print("ERROR, please enter an int!")
        return False


def get_input(board: list, player: int) -> int:
    input_num = input("Please enter a number from the list above: ")
    if verify_int(input_num):
        number = int(input_num)-1
        print()
    else:
        if input_num == "quit":
            game_over()
        else:
            print("ERROR, Please enter an integer!", end="\n\n")
            return get_input(board, player)

    available_moves = check_columns(board)
    if number in available_moves:
        return int(number)
    else:
        print("ERROR, Please enter a number from the list above!")
        return get_input(board, player)


def game_over(player: int = None) -> None:
    if player is None:
        print("You quit the game")
    else:
        player_letter = "X" if player == 1 else "O"
        print(f"The game is over!\nPlayer {player_letter} wins!")
    quit()


def start() -> None:
    print(
        f"\nWelcome to Connect {CONNECTED}! (type 'quit' to exit)", end="\n\n\n")
    answer = input("Would you like to play multiplayer? (Y/N): ")
    multiplayer = True if answer == "Y" else False

    board = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
    display(board)
    player = -1
    run(board, player, multiplayer)


def run(board: list, player: int, multiplayer: bool) -> None:
    while not check_game(board):
        if player == 1:
            player = -1
            print("Player O's move is next")
            if multiplayer:
                user_input = human_input(board, player)
            else:
                user_input = npc_input(board, player)

        elif player == -1:
            player = 1
            print("Player X's move is next")
            user_input = human_input(board, player)

        board = move(board, user_input, player)
        display(board)
    else:
        game_over(player)


def npc_input(board: list, player: int) -> int:
    available_moves = check_columns(board)
    rand_input = r_int(0, len(available_moves)-1)
    player_input = available_moves[rand_input]
    return player_input


def human_input(board: list, player: int) -> int:
    available_moves = ', '.join(str(x+1) for x in check_columns(board))
    print(f"You can slot into one of the following columns: {available_moves}")
    user_input = get_input(board, player)
    return user_input


ROWS = 6
COLUMNS = 7
CONNECTED = 4

ASK_FOR_DIMENTIONS = True

if ASK_FOR_DIMENTIONS:
    ROWS = ask_for_dimentions("ROWS")
    COLUMNS = ask_for_dimentions("COLUMNS")
    CONNECTED = ask_for_dimentions("CONNECTED")

start()
