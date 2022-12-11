from dataclasses import dataclass


@dataclass
class Monkey:
    """
    Main class based solution containing methods for solving Day Eleven of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.items = []  # List containing all item worry levels
        self.divisible_by = 1  # The integer to divide by in the `test`
        self.inspections = 0  # The number of times a monkey has inspected an item
        self.operation = ""  # The operation performed on a given item
        self.throws = [1, 1]  # The corresponding monkey ID to throw on a pass or fail of the test
