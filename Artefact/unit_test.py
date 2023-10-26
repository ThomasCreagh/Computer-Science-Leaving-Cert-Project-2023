from game import ConnectX
import csv

game = ConnectX(6, 7, 4, ("bot", "bot"))


def unit_tests(function, test_file: str, answer_file: str) -> None:
    """Tests functions from the main program

    Args:
        function (Function): function to test
        test_file (str): path to the test file
        answer_file (str): path to the answer file
    """

    func_name = str(function).split(" ")[1]
    print(f"Testing the function: {func_name}...")

    with open(test_file, "r") as test_file, \
            open(answer_file, "r") as answer_file:

        success = 0
        fails = 0

        test_csv_data = csv.reader(test_file)
        test_data = list(test_csv_data)

        answer_csv_data = csv.reader(answer_file)
        answer_data = list(answer_csv_data)

        for i in range(len(answer_data)):
            print(f"test {i+1}:", end=" ")
            matrix = []
            for j in range(len(test_data[0][0:-2])):
                filtered = list(filter(lambda x: True if x not in "[], "
                                       else False, test_data[i][j]))
                integer_list = list(map(lambda x: int(x), filtered))
                matrix += [integer_list]

            game.board = matrix
            answer_output = str()

            if answer_data[i] == ['True']:
                answer_output = True
            else:
                answer_output = False

            game.board = matrix
            output = game.check_game()
            if output == answer_output:
                print("success")
                success += 1
            else:
                print("fail")
                fails += 1

        print("\ntotal successes:", success)
        print("total fails:", fails)


unit_tests(ConnectX.check_game, "data/test_data.csv", "data/answer_data.csv")
