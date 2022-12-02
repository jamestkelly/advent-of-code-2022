from copy import copy


class CalorieCounter:
    """
    Main class based solution containing methods for solving Day One of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.meals = []
        self.construct_data('input.txt')

    def construct_data(self, file_name: str) -> None:
        """
        Constructs the data set provided in `input.txt` into a list of meals as sub-lists.

        :param file_name: The file name to read into memory.
        """
        with open(file_name) as file_object:
            elf = []
            for line in file_object:
                line.strip()
                if line == "" or line == "\n":
                    self.meals.append(copy(elf))
                    elf.clear()
                else:
                    elf.append(int(line))

    def elf_max(self) -> int:
        """
        Fetches the meal carried by any given elf with the maximum amount of calories. This is the solution for Part One
        of Day One.

        :return: The maximum amount of calories for a meal carried by an individual elf.
        """
        return max([sum(elf) for elf in self.meals])

    def greediest_elves(self) -> int:
        """
        Fetches the top three meals in terms of calorie count and sums them. This is the solution for Part Two of Day
        One.

        :return:  The sum of the top three meals in terms of calorie count.
        """
        return sum(sorted([sum(elf) for elf in self.meals], reverse=True)[:3])

    def print_results(self) -> None:
        """
        Prints the results to the console.
        """
        max_elf = self.elf_max()
        elves_greediest = self.greediest_elves()
        print(f'Answer to Part 1: {max_elf}\n---')
        print(f'Answer to Part 2: {elves_greediest}')


if __name__ == "__main__":
    calories = CalorieCounter()
    calories.print_results()
