class DayNine:
    """
    Main class based solution containing methods for solving Day Eight of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.data = self.construct_data("input.txt")

    @staticmethod
    def construct_data(file_name: str) -> list:
        """
        Constructs the data set provided in `input.txt` into a list of section assignment pairs.

        :param file_name: The file name to read into memory.
        :return: A list containing the `assignment pairs` to be searched.
        """
        with open(file_name, 'r') as file_object:
            data = [row.strip() for row in file_object.readlines()]
            grid_map = []

            for row in data:
                grid_map.append([eval(row) for row in [*row]])

        return grid_map

    def part_one_search(self) -> int:
        """


        :return:
        """
        pass

    def part_two_search(self) -> int:
        """


        :return:
        """
        pass

    def solve(self) -> None:
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_search())
        print("Part Two (2):", self.part_two_search())


if __name__ == "__main__":
    nine = DayNine()
    nine.solve()
