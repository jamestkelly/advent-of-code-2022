import math


class RucksackReorganisation:
    """
    Main class based solution containing methods for solving Day Three of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.rucksacks = self.construct_data("input.txt")

    @staticmethod
    def construct_data(file_name: str) -> list:
        """
        Constructs the data set provided in `input.txt` into a list of hands as strings.

        :param file_name: The file name to read into memory.
        :return: A list containing the `rucksacks` to be searched.
        """
        with open(file_name) as file_object:
            data = file_object.read().strip()  # Open data object and strip whitespaces
            return data.split("\n")  # Return the data object as a list split by new lines

    @staticmethod
    def generate_priority(intersect: set) -> int:
        """
        Generates the `priority` of the given item within the rucksack through converting values of the ASCII alphabetic
        character to an `ord`.

        :param intersect: The intersection of the rucksack sets.
        :return: An integer representing the priority of the item.
        """
        item = list(intersect)[0]  # Unwrap the set to a single character as a string
        if item.islower():  # Check if the character is lowercase
            return ord(item) - ord("a") + 1
        else:
            return ord(item) - ord("A") + 27

    def part_one_search(self) -> int:
        """
        Performs the search between two `compartments` of a `rucksack` to determine an intersect between the two sets.
        This method treats each data access object (DAO) as a set and uses set theory to determine the correlating
        values that are of the highest `priority` as per the stipulations of the problem statement. This method then
        returns the sum of all highest priority items per `rucksack`.

        :return: The sum of the total priority when combining each priority item per `rucksack`.
        """
        total_priority = 0

        for rucksack in self.rucksacks:
            compartment_length = math.floor(len(rucksack) / 2)
            first_compartment, second_compartment = rucksack[:compartment_length], rucksack[compartment_length:]
            intersect = set(list(first_compartment)) & set(list(second_compartment))
            total_priority += self.generate_priority(intersect)

        return total_priority

    def part_two_search(self) -> int:
        """
        This method is similar to the `part_one_search` method with the difference is that it finds intersects
        between `rucksacks` grouped in threes (3) and returns the sum of the total `priority` based on the items found
        across the entire dataset.

        :return: The total sum priority of the items found to intersect every group of three (3) `rucksacks`.
        """

        total_priority = 0

        for index in range(0, len(self.rucksacks), 3):
            intersect = set(self.rucksacks[index]) & set(self.rucksacks[index + 1]) & set(self.rucksacks[index + 2])

            total_priority += self.generate_priority(intersect)

        return total_priority

    def solve(self) -> None:
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_search())
        print("Part Two (2):", self.part_two_search())


if __name__ == "__main__":
    rucksack_reorganisation = RucksackReorganisation()
    rucksack_reorganisation.solve()
