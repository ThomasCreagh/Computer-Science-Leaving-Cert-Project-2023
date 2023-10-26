from game import ConnectX
import analyses

from datetime import datetime


class Start:

    """Starts the game and sets up the game to run
    """

    def __init__(self,
                 filename=f"data/data-{datetime.now():%Y-%m-%d_%H-%M-%S}.csv"):
        """Starts the game and it is responsible for
        taking the first dimension inputs for the game

        Args:
            filename (str, optional): The filename of the current log file.
                Defaults to "data.csv".
        """
        self.filename = filename
        self.welcome_message()

    def welcome_message(self) -> None:
        """Welcomes the user and displays the rules
        """
        print("Welcome to ConnectX!")
        print("enter 'quit' to exit")
        print("View in a full-screen console for the best experience\n")

        rules = self.small_input_check(
            "Would you like to view the rules?(y/n): ",
            ["y", "n"])
        if rules == "y":
            print("\nRULES:\n"
                  "You can slot from the top\n"
                  "The pieces stacks on top of each other\n"
                  "Each person goes one after another\n"
                  "The game is over when a player gets x\n"
                  "number of pieces in a row\n")

        play_or_data = self.small_input_check(
            "Would you like to play the game or "
            "view the auto-collection data?(play/data): ",
            ["play", "data"])

        if play_or_data == "play":
            self.dimension_check()
            self.selection()

        else:
            analyses.game_analytics("data/automatic_data_collection.csv")

    def dimension_check(self):
        """Asks for custom dimensions
        """

        answer = self.small_input_check(
            "Would you like to have custom dimension?(y/n): ",
            ["y", "n"])

        self.check_for_quit(answer)

        if answer == "y":
            self.dimensions()

        elif answer == "n":
            self.COLUMNS = 7
            self.ROWS = 6
            self.CONNECTIONS = 4
            self.PLAYERS_SELECTED = self.small_input_check(
                "Please select an option: \n"
                "Single-player(1), Multi-player(2), Simulation-play(3): ",
                ["1", "2", "3"])

            self.check_for_quit(self.PLAYERS_SELECTED)
            self.PLAYERS_SELECTED = int(self.PLAYERS_SELECTED)

    def check_for_quit(self, _input: str) -> bool:
        """Checks if the player has decided to quit

        Args:
            _input (str): check if input includes a quit

        Returns:
            bool: If program is not quit
        """

        if _input in ["quit", "exit"]:
            print("You quit the game")
            quit()
        else:
            return False

    def small_input_check(
            self, prompt: str, _list: list = None,
            function: list = None) -> any:
        """Gets an input till requirements from a function or in a list is met

        Args:
            prompt (str): Prompt given to the user
            _list (list, optional): List of options.
                Defaults to None.
            function (list, optional): Function to call with output arg.
                Defaults to None.

        Returns:
            any: the original input
        """

        output = input(prompt)
        if _list is not None:
            while output not in _list:
                self.check_for_quit(output)
                self.print_error()
                output = input(prompt)
            return output
        elif function is not None:
            while not function(output):
                self.check_for_quit(output)
                self.print_error()
                output = input(prompt)
            return output
        else:
            print("major error in function: 'small_input_check'")

    def validation_value(self) -> bool:
        """Checks if the game has valid values

        Returns:
            bool: True if valid values, otherwise False
        """

        if self.COLUMNS < 1 or self.ROWS < 1 or self.CONNECTIONS < 1:
            return False
        if (self.COLUMNS > 10000 or self.ROWS > 10000
                or self.CONNECTIONS > 10000):
            return False
        if self.CONNECTIONS > self.COLUMNS and self.CONNECTIONS > self.ROWS:
            return False
        if self.PLAYERS_SELECTED not in [1, 2, 3, 4]:
            return False

        return True

    def validation_of_int(self, _input: any) -> bool:
        """Validation function that makes the input an int if it is valid

        Args:
            _input (any): the input to validate

        Returns:
            bool: whether the input can be made into an integer
        """

        if _input.isnumeric():
            return True
        else:
            return self.check_for_quit(_input)

    def print_error(self) -> None:
        """Prints the error to the console
        """

        print()
        print("This input is not valid!")
        print("Please try again")
        print()

    def validation_manager(self) -> bool:
        """Manages all the different validation functions

        Returns:
            bool: If variable valid it returns True, otherwise False
        """

        for i in [self.COLUMNS, self.ROWS, self.CONNECTIONS,
                  self.PLAYERS_SELECTED]:
            if not self.validation_of_int(i):
                self.print_error()
                return False

        self.COLUMNS = int(self.COLUMNS)
        self.ROWS = int(self.ROWS)
        self.CONNECTIONS = int(self.CONNECTIONS)
        self.PLAYERS_SELECTED = int(self.PLAYERS_SELECTED)

        if not self.validation_value():
            self.print_error()
            return False

        return True

    def dimensions(self) -> None:
        """Gets the dimensions of the grid,
        connected symbols and what mode that they want
        """

        running = False
        while not running or not self.validation_manager():
            print("What size grid would you like?")
            self.COLUMNS = input("Columns: ")
            self.check_for_quit(self.COLUMNS)

            self.ROWS = input("Rows: ")
            self.check_for_quit(self.ROWS)

            self.CONNECTIONS = input("Connected symbols to win: ")
            self.check_for_quit(self.CONNECTIONS)

            print("Please select an option: ")
            self.PLAYERS_SELECTED = input(
                "Single-player(1), Multi-player(2), Simulation-play(3): ")
            self.check_for_quit(self.PLAYERS_SELECTED)
            running = True

    # fix quit, add original mode too
    def selection(self) -> None:
        """Figure out the options of the games with conditionals,
        and runs necessary functions
        """

        if self.PLAYERS_SELECTED == 1:
            turn = self.small_input_check("Would you like to go first?(y/n): ",
                                          ["y", "n"])
            self.check_for_quit(turn)

            if turn == "y":
                game = ConnectX(self.ROWS, self.COLUMNS,
                                self.CONNECTIONS, ("user", "bot"))
                game.run()
            elif turn == "n":
                game = ConnectX(self.ROWS, self.COLUMNS,
                                self.CONNECTIONS, ("bot", "user"))
                game.run()

        elif self.PLAYERS_SELECTED == 2:
            game = ConnectX(self.ROWS, self.COLUMNS,
                            self.CONNECTIONS, ("user", "user"))
            game.run()

        elif self.PLAYERS_SELECTED == 3:
            iterations = int(self.small_input_check(
                "How many games would you like to run?: ",
                function=self.validation_of_int))

            for _ in range(iterations):
                game = ConnectX(self.ROWS, self.COLUMNS, self.CONNECTIONS,
                                ("bot", "bot"), True, self.filename)
                game.run()

            probabilities, draws = analyses.get_probabilities(self.filename)
            print("Total draws:", draws, end=" ")
            print("out of", iterations)
            print("Probabilities:", probabilities)
        else:
            print("major error in function: 'selection'")
