import copy


class SupplyStacks:
    """
    Main class based solution containing methods for solving Day Five of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.crates = []
        self.moves = []
        self.construct_data("input.txt")
        self.solve()

    def construct_data(self, file_name: str) -> None:
        """
        Constructs & parses the data from the supplied input. This method was created in the cleanup process of the code
        as previously the `crates` were hardcoded as a global variable.
        """
        with open(file_name, 'r') as file_object:
            raw_crates, raw_lines = file_object.read().split("\n\n")
            instructions = raw_lines.splitlines()

        self.crates = [[] for _ in range(10)]  # Create an empty nested list with the total number of columns

        for row in raw_crates.splitlines()[-2::-1]:  # Iterate through all crates
            for index, crate in enumerate(row[1::4], start=1):  # Crates appear every four (4) characters
                if crate != " ":  # If the crate is not an empty string
                    self.crates[index].append(crate)  # Append the crate for the column to the object

        self.generate_moves(instructions)

    @staticmethod
    def format_result(crates: list) -> str:
        """
        Conforms the output of the solution from a list to string for printing results to the console in a format that
        is acceptable for submission.

        :return: A string containing the top rows of each column.
        """
        top_row = [crate[-1] for crate in crates[1:]]  # Fetch the top row of each column
        result = ""

        for crate in top_row:
            result += crate

        return result

    def generate_moves(self, instructions: list) -> None:
        """
        Parses the moves from the format of `move 2 from 7 to 2` to a tuple containing integers representing the:
            - Crates
            - Source
            - Destination
        """
        for row in instructions:
            row = row.split()
            self.moves.append(tuple(map(int, (row[1], row[3], row[5]))))  # Map integers to a tuple

    def part_one_simulate(self) -> str:
        """
        Performs a search to find a respective `crate` in a given `stack` (treated as a literal stack), which is then
        popped from the list of `crates` in the `source` and appended to the `destination`.

        :return: The crates after being `moved` by the `crane`.
        """
        crates = copy.deepcopy(self.crates)

        for num_crates, _from, _to in self.moves:
            for _ in range(num_crates):
                crates[_to].append(crates[_from].pop())

        return self.format_result(crates)

    def part_two_simulate(self) -> str:
        """
        Similar to `part_one_simulate` this method extends the `destination` rather than appends and then deletes the
        corresponding `crates` from the `source` directory.

        :return: The crates after being `moved` by the `crane`.
        """
        crates = copy.deepcopy(self.crates)

        for num_crates, _from, _to in self.moves:
            crates[_to].extend(crates[_from][-num_crates:])
            del crates[_from][-num_crates:]

        return self.format_result(crates)

    def solve(self) -> None:
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_simulate())
        print("Part Two (2):", self.part_two_simulate())


if __name__ == "__main__":
    supply = SupplyStacks()
