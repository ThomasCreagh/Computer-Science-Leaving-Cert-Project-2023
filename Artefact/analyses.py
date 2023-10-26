import csv
from math import sqrt
import matplotlib.pyplot as plt
import seaborn as sns


def get_probabilities(file_name: str = "data.csv") -> None:
    """Analyses the data and find the most optimal
        first move based on that data

    Args:
        file_name (str): the name of the file

    Returns:
        list: probabilities of each column
        int: number of draws
    """

    with open(file_name, "r") as _file:
        csv_data = csv.reader(_file)
        data = list(csv_data)
        col_ratio = []
        total_draws = 0
        col_amount = 0

        for i in data[0][0]:
            if i.isnumeric():
                col_amount += 1

        # comment
        for col in range(1, col_amount + 1):
            win = 0
            lose = 0
            draw = 0
            for row in data:
                if int(row[-2]) == col:
                    if row[-1] == "1":
                        win += 1
                    elif row[-1] == "0":
                        lose += 1
                    else:
                        draw += 1
            col_ratio += [(win, lose)]
            total_draws += draw

        col_probability = []
        for i in range(len(col_ratio)):
            if (col_ratio[i][0] + col_ratio[i][1]) == 0:
                col_probability += [None]
            else:
                col_probability += [(col_ratio[i][0])
                                    / (col_ratio[i][0]
                                    + col_ratio[i][1])]

        col_list = [i for i in range(1, len(col_probability) + 1)]

        plt.plot(col_list, col_probability)
        plt.title("Probability of winning based "
                  "on what column you played first")
        plt.xlabel("Columns")
        plt.ylabel("Probability")
        plt.show()

        return col_probability, total_draws


def game_analytics(
        file_name: str = "data/automatic_data_collection.csv") -> None:
    """This function is used to analyze the data in every game

    Args:
        file_name (str): the name of the file

    Returns:
        list: data[int: total number of horizontally won games,
                   int: total number of vertically won games,
                   int: total number of diagonally won games,
                   int: total number of draws,
                   int: mean number of moves per game,
                   int: median number of moves per game,
                   int: standard deviation of moves per game]
    """

    with open(file_name, "r") as _file:
        csv_data = csv.reader(_file)
        data = list(csv_data)

        horizontal_sum = 0
        vertical_sum = 0
        diagonal_sum = 0
        draw_sum = 0

        all_moves = []

        for i in range(len(data)):
            all_moves += [int(data[i][0])]

            if data[i][1] == "H":
                horizontal_sum += 1
            elif data[i][1] == "V":
                vertical_sum += 1
            elif data[i][1] == "D":
                diagonal_sum += 1
            else:
                draw_sum += 1

        all_moves.sort()

        if len(all_moves) % 2 == 0:
            median_moves = (all_moves[len(all_moves)//2]
                            + all_moves[(len(all_moves)//2)-1]) / 2
        else:
            median_moves = all_moves[len(all_moves)//2]

        mean_moves = sum(all_moves)/len(data)
        standard_deviation_list = [(i-mean_moves)**2 for i in all_moves]
        standard_deviation = round(sqrt(sum(standard_deviation_list)
                                        / (len(data)-1)), 3)
        mean_moves = round(mean_moves, 3)

        mode_moves = max(set(all_moves), key=all_moves.count)

        odd_list = sum([i for i in all_moves if i % 2 == 0])
        even_list = sum([i for i in all_moves if i % 2 == 1])

        plt.hist(all_moves, color="lightblue", ec="black", bins=35)
        plt.xlabel("number of moves per game")
        plt.ylabel("frequency")

        sns.displot(data=all_moves, kind="kde")
        plt.xlabel("number of moves per game")
        plt.ylabel("frequency")

        sns.displot(data=all_moves, kde=True, bins=35)
        plt.xlabel("number of moves per game")
        plt.ylabel("frequency")

        print("\nDATA:\n"
              f"Games Horizontally won: {horizontal_sum}\n"
              f"Games Vertically won: {vertical_sum}\n"
              f"Games Diagonally won: {diagonal_sum}\n"
              f"Games drew: {draw_sum}\n"
              f"Mean moves per game: {mean_moves}\n"
              f"Median moves per game: {median_moves}\n"
              f"Mode moves per game: {mode_moves}\n"
              "Standard deviation of moves per game: "
              f"{standard_deviation}\n"
              "The number of an odd number of moves won: "
              f"{odd_list}\n"
              "The number of an even number of moves won: "
              f"{even_list}\n"
              "The chance that the first player would win the game: "
              f"{odd_list/(even_list+odd_list)}\n"
              "The chance that the second player would win the game: "
              f"{even_list/(even_list+odd_list)}\n")

        plt.show()
