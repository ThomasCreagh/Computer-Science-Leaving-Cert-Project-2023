from random import randint as r_int
import csv


class ConnectX:

    """This class is the game model,
        it runs the game through different functions throughout
    """

    def __init__(self, rows: int, columns: int, connected: int, players: tuple,
                 log: bool = False, filename: str = "data.csv") -> None:
        """
        The __init__ function is an in-built function
            in python to declare the class variables

        Args:
            rows (int): number of rows
            columns (int): number of columns
            connected (int): number of connected symbols
            players (tuple): either "bot" or "user"
            log (bool): whether to log statistics
            Defaults to False.
            filename (str, optional): The filename of the current log file.
                Defaults to "data.csv".
        """

        self.ROWS = rows
        self.COLUMNS = columns
        self.CONNECTED = connected
        self.PLAYERS = players
        self.LOG = log
        self.LOG_FILE_NAME = filename

        self.win_type = "N"
        self.num_of_moves = 0
        self.first_move = None
        self.board = [[0 for _ in range(self.COLUMNS)]
                      for _ in range(self.ROWS)]
        self.player = 2

    def display(self) -> None:
        """
        Displays the board to the console based on the board matrix
        """

        print("\t", end="")
        for i in range(1, self.COLUMNS + 1):
            print(i, end="\t")
        print("\n" * 3)

        for i in range(self.ROWS):
            print(i + 1, end="\t")
            for j in range(self.COLUMNS):
                if self.board[i][j] == 2:
                    print("O", end="\t")
                elif self.board[i][j] == 1:
                    print("X", end="\t")
                elif self.board[i][j] == 0:
                    print(".", end="\t")
                else:
                    print("?", end="\t")
            print("\n" * 3)
        print()

    def check_columns(self) -> list:
        """
        Checks the top row to the board
            to figure out what columns aren't full

        Returns:
            list: the board matrix
        """

        moves = [i for i in range(len(self.board[0])) if self.board[0][i] == 0]
        return moves

    def move(self, column: int) -> list:
        """
        Based on the column selected to
            insert they're piece, the board will update

        Returns:
            list: updated board matrix
        """

        new_board = self.board

        for i in range(self.ROWS - 1, -1, -1):
            if new_board[i][column] == 0:
                new_board[i][column] = self.player
                break

        return new_board

    def check_for_quit(self, _input: str) -> bool:
        """
        Checks if the player has decided to quit

        Returns:
            bool: if not quitting
        """

        if _input in ["quit", "exit"]:
            print("You quit the game")
            quit()
        else:
            return False

    def check_game(self) -> bool:
        """
        Checks if the game is over either vertically,
            horizontally, diagonally or is a draw

        Returns:
            bool: True if the game is over otherwise False
        """

        for row in self.board:
            for col in range(len(self.board[0]) - self.CONNECTED + 1):
                if row[col] != 0:
                    outcome = True
                    for num_c in range(col, self.CONNECTED + col - 1):
                        if row[num_c] != row[num_c + 1]:
                            outcome = False
                    if outcome:
                        self.win_type = "H"
                        return True

        for col in range(len(self.board[0])):
            for row in range(len(self.board) - self.CONNECTED + 1):
                if self.board[row][col] != 0:
                    outcome = True
                    for num_r in range(row, self.CONNECTED + row - 1):
                        if (self.board[num_r][col]
                                != self.board[num_r + 1][col]):
                            outcome = False
                    if outcome:
                        self.win_type = "V"
                        return True

        for row in range(len(self.board) - self.CONNECTED + 1):
            for col in range(len(self.board[0]) - self.CONNECTED + 1):
                if self.board[row][(len(self.board[0]) - col) - 1] != 0:
                    outcome = True
                    for num_r, num_c in zip(
                        range(row, self.CONNECTED + row - 1),
                        range(col, (self.CONNECTED
                                    + len(self.board[0]) - col) - 2)):
                        if (self.board[num_r][(len(self.board[0]) - num_c) - 1]
                                != (self.board[num_r + 1]
                                    [(len(self.board[0]) - num_c) - 2])):
                            outcome = False
                    if outcome:
                        self.win_type = "D"
                        return True

                if self.board[row][col] != 0:
                    outcome = True
                    for num_r, num_c in zip(
                            range(row, self.CONNECTED + row - 1),
                            range(col, self.CONNECTED + col - 1)):
                        if (self.board[num_r][num_c]
                                != self.board[num_r + 1][num_c + 1]):
                            outcome = False
                    if outcome:
                        self.win_type = "D"
                        return True

        if 0 in self.board[0]:
            return False

        self.win_type = "N"
        return True

    def get_input(self) -> int:
        """Gets the input from the human user

        Returns:
            int: the input value which is validated
        """

        number = input("Please enter a number from the list above: ")
        available_moves = self.check_columns()

        while number not in ([str(i + 1) for i in available_moves]
                             + ["quit", "exit"]):
            print("ERROR, Please enter a number from the list above!")
            number = input("Please enter a number from the list above: ")

        self.check_for_quit(number)

        return int(number) - 1

    def game_over(self, _type: int = None) -> None:
        """Deals with the game being over or exited

        Args:
            _type (int): the type of game over
                Defaults to None.
        """

        if _type == "quit":
            print("You quit the game")
        elif _type == "won":
            player_letter = "X" if self.player == 1 else "O"
            print("The game is over!"
                  f"\nPlayer {player_letter} wins!") if not self.LOG else None
            self.log()
        elif _type == "draw":
            print("The game is over!\n"
                  "There was no winner because it was a draw!"
                  ) if not self.LOG else None
            self.log(True)

    def run(self) -> None:
        """The main run loop
        """

        self.display() if not self.LOG else None
        while not self.check_game():
            self.num_of_moves += 1
            if self.player == 1:
                self.player = 2
                print("Player O's move is next") if not self.LOG else None
            elif self.player == 2:
                self.player = 1
                print("Player X's move is next") if not self.LOG else None
            else:
                self.game_over("won")

            if self.PLAYERS[self.player - 1] == "user":
                user_input = self.human_input()
            elif self.PLAYERS[self.player - 1] == "bot":
                user_input = self.npc_input()
            else:
                print("Fatal error: invalid player input in the run.py file")
                break

            if self.LOG and self.first_move is None:
                self.first_move = user_input + 1

            self.board = self.move(user_input)
            self.display() if not self.LOG else None
        else:
            if 0 not in self.board[0]:
                self.game_over("draw")
            else:
                self.game_over("won")

    def npc_input(self) -> int:
        """Non-player-character that randomly
            selects one of the available columns

        Returns:
            int: column selected by the npc
        """

        available_moves = self.check_columns()
        rand_input = r_int(0, len(available_moves) - 1)
        player_input = available_moves[rand_input]
        return player_input

    def human_input(self) -> int:
        """Gets the human input from the user it also
            displays the available columns to input into

        Returns:
            int: column selected by the human user
        """

        available_moves = ", ".join(str(x + 1) for x in self.check_columns())
        print("You can slot into one of the following columns: "
              f"{available_moves}")
        user_input = self.get_input()
        return user_input

    def log(self, draw: bool = False) -> None:
        """Logs the end state of the game to a
            csv file (only runs if self.LOG is enabled)

        Args:
            draw (bool): True if the game was a draw, otherwise False
                Defaults to False
        """

        if self.LOG:
            with open(self.LOG_FILE_NAME, "a", newline="\n") as _file:
                data_writer = csv.writer(_file)
                if not draw:
                    if self.player == 2:
                        data_writer.writerow(list(self.board)
                                             + [self.first_move, 1])
                    else:
                        data_writer.writerow(list(self.board)
                                             + [self.first_move, 0])
                else:
                    data_writer.writerow(list(self.board)
                                         + [self.first_move, 2])
        with open("data/automatic_data_collection.csv",
                  "a", newline="\n") as _file:
            data_writer = csv.writer(_file)
            data_writer.writerow([self.num_of_moves, self.win_type])
