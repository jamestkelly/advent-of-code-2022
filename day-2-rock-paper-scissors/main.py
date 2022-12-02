class RockPaperScissors:
    """
    Main class based solution containing methods for solving Day Two of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables. Note: I hardcoded the values for comparisons to make it more simple.
        """
        self.part_one_values = {
            'A X': 4,
            'A Y': 8,
            'A Z': 3,
            'B X': 1,
            'B Y': 5,
            'B Z': 9,
            'C X': 7,
            'C Y': 2,
            'C Z': 6,
        }
        self.part_two_values = {
            "A X": 3,
            "A Y": 4,
            "A Z": 8,
            "B X": 1,
            "B Y": 5,
            "B Z": 9,
            "C X": 2,
            "C Y": 6,
            "C Z": 7
        }
        self.hands = self.construct_data("input.txt")
        self.play_game()

    @staticmethod
    def construct_data(file_name: str) -> list:
        """
        Constructs the data set provided in `input.txt` into a list of hands as strings.

        :param file_name: The file name to read into memory.
        :return: A list containing the `hands` to be played.
        """
        with open(file_name) as file_object:
            return [line.strip() for line in file_object.readlines()]

    def part_one_game(self) -> int:
        """
        Method to sum the total number of points scored following the rules outlined in the attached `README.md`.

        :return: The total score.
        """
        return sum(self.part_one_values[index] for index in self.hands)

    def part_two_game(self) -> int:
        """
        Method to sum the total number of points scored following the rules outlined in the attached `README.md`.

        :return: The total score.
        """
        return sum(self.part_two_values[index] for index in self.hands)

    def play_game(self) -> None:
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_game())
        print("Part Two (2):", self.part_two_game())


if __name__ == "__main__":
    rock_paper_scissors = RockPaperScissors()
