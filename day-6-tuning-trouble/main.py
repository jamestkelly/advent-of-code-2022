class TuningTrouble:
    """
    Main class based solution containing methods for solving Day Six of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.chunk = []
        self.construct_data("input.txt")

    def construct_data(self, file_name: str) -> None:
        """
        Constructs & parses the data from the supplied input.
        """
        with open("input.txt", 'r') as file_object:
            self.chunk = file_object.read().strip()

    def make_message(self, index: int, packet_size: int) -> set:
        """
        Converts a given `packet` (series of random characters) to an immutable set whereby all duplicates are removed.
        """
        return set(self.chunk[index:index + packet_size])

    def trace_packet(self, packet_size: int) -> int:
        """
        Iterates through all `packets` of a given size and returns the amount of iterations encountered before finding a
        `marker`, i.e., a series of characters that contains no duplicates matching to the supplied `packet_size`.

        :param packet_size: The length of the packet to search for.
        :return: An integer corresponding to the number of iterations before finding the `marker` signifying the end of
            the packet.
        """
        for index in range(len(self.chunk) - packet_size):
            message = self.make_message(index, packet_size)
            if len(message) is packet_size:
                return index + packet_size

    def part_one_trace(self) -> int:
        """
        Searches for the `marker` given a `packet_size` of four (4).

        :return: An integer corresponding to the number of iterations before finding the `marker`.
        """
        return self.trace_packet(4)

    def part_two_trace(self):
        """
        Searches for the `marker` given a `packet_size` of fourteen (14).

        :return: An integer corresponding to the number of iterations before finding the `marker`.
        """
        return self.trace_packet(14)

    def solve(self) -> None:
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_trace())
        print("Part Two (2):", self.part_two_trace())


if __name__ == "__main__":
    tuning = TuningTrouble()
    tuning.solve()
