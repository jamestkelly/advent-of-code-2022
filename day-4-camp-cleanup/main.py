import re


class CampCleanup:
    def __init__(self) -> None:
        self.data = self.construct_data("input.txt")

    @staticmethod
    def construct_data(file_name: str) -> list:
        """
        Constructs the data set provided in `input.txt` into a list of section assignment pairs.

        :param file_name: The file name to read into memory.
        :return: A list containing the `assignment pairs` to be searched.
        """
        with open(file_name) as file_object:
            return [line for line in file_object.read().splitlines()]

    @staticmethod
    def map_data(data_set):
        """
        Maps the `assignment pairs` contained within a given line of data to individual integers, e.g., if provided the
        line, `26-80,26-90` then it returns: `a = 26`, `b = 80`, `c = 26`, and `d = 90`. The method then creates a list
        or array filling the `range` between both `a` and `b`, and `c` and `d` and returns them as two immutable `sets`.

        :param data_set: The input data containing the assignment pairs.
        :return: Two sets containing the range of values for both assignment pairs contained in the line from the data.
        """
        id_a, id_b, id_c, id_d = map(int, re.findall(r'\d+', data_set))
        return set(range(id_a, id_b + 1)), set(range(id_c, id_d + 1))

    def part_one_search(self) -> int:
        """
        Searches through every line contained within the input data and checks if either assignment, the range of ID
        numbers, is a subset of the other assignment contained within the line.

        :return: The total number of subsets found.
        """
        subsets = 0
        for data_set in self.data:
            pair_one, pair_two = self.map_data(data_set)
            subsets += pair_one.issubset(pair_two) or pair_two.issubset(pair_one)

        return subsets

    def part_two_search(self) -> int:
        """
        Similar to the `part_one_search()`, this method searches through every line contained within the input data and
        checks if there are any intersections between the two assignment ranges via the `any()` method.

        :return: The total number of intersections found.
        """
        intersections = 0
        for data_set in self.data:
            pair_one, pair_two = self.map_data(data_set)
            intersections += any(pair_one.intersection(pair_two))

        return intersections

    def solve(self) -> None:
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_search())
        print("Part Two (2):", self.part_two_search())


if __name__ == "__main__":
    camp_clean = CampCleanup()
    camp_clean.solve()
