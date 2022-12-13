class DistressSignal:
    """
    Main class based solution containing methods for solving Day Thirteen of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.packet_pairs = []
        self.construct_data("input.txt")

    @staticmethod
    def match_condition(left: any, right: any) -> int or None:
        """
        Extracted conditional comparison method to perform comparisons corresponding to the problem statement.

        :param left: A list or integer containing the first or left-most packet in the data.
        :param right: A list or integer containing the second or right-most packet in the data.
        :return: An integer or None, respective to the result of the comparison.
        """
        if isinstance(left, int) and isinstance(right, int):  # Both packets are integers
            return 0
        elif isinstance(left, list) and isinstance(right, list):  # Both packets are lists
            return -1
        elif isinstance(left, int):  # Only the left packet is an integer
            return 1
        else:  # Only the right packet is an integer
            return None

    def construct_data(self, file_name: str) -> None:
        """
        Similar to previous days' solutions, this method reads a file into memory and parses the data to an acceptable
        format for solving the problem statement. This method specifically converts the input `packets`, i.e.,
            `[[1],[2,3,4]]`
            `[[1],4]`
        To a `list` format, whereby both the `left` and `right` packets are converted to lists.

        :param file_name: The file name to read into memory.
        """
        with open(file_name, 'r') as file_object:
            data = file_object.read().strip().split("\n\n")
            self.packet_pairs = [[eval(line) for line in packets.splitlines()] for packets in data]

    def compare_packets(self, left, right) -> int or bool or None:
        """
        Recursive method to compare each `left` and `right` packet contained within the dataset. This method follows the
        rules set out by the problem statement, whereby:
        - If both values are integers, the lower integer should come first.
        - If the left integer is lower than the right integer, the inputs are in the right order.
        - If the left integer is higher than the right integer, the inputs are not in the right order.
        - Otherwise, the inputs are the same integer; continue checking the next part of the input.
        - If both values are lists, compare the first value of each list, then the second value, and so on.
        - If the left list runs out of items first, the inputs are in the right order.
        - If the right list runs out of items first, the inputs are not in the right order.
        - If the lists are the same length and no comparison makes a decision about the order, continue checking input.
        - If exactly one value is an integer, convert the integer to a list, then retry the comparison.
        For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is
        then found by instead comparing [0,0,0] and [2].

        :param left: A list or integer containing the first or left-most packet in the data.
        :param right: A list or integer containing the second or right-most packet in the data.
        :return: An integer, boolean, or None, respective to the result of the recursive comparisons.
        """
        match self.match_condition(left, right):
            case 0:  # Both packets are integers
                if left == right:
                    return None
                return left < right
            case -1:  # Both packets are lists
                for a, b in zip(left, right):  # Create an iterator of tuples to loop through simultaneously
                    comparison = self.compare_packets(a, b)  # Compare the packets
                    if comparison is not None:
                        return comparison
                return self.compare_packets(len(left), len(right))  # Recursive call to continue searching via length
            case 1:  # Only the left packet is an integer
                return self.compare_packets([left], right)  # Convert left packet to list and recursive call
            case _:  # Only the right packet is an integer
                return self.compare_packets(left, [right])  # Convert right packet to list and recursive call

    def part_one_search(self) -> int:
        """
        Determines which of the pairs in the input data are in the `correct` order and produces the sum of the indices
        of the pairs that are in order.

        :return: An integer corresponding to the sum of the indices of pairs that are in order.
        """
        return sum(i for i, (left, right) in enumerate(self.packet_pairs, 1) if self.compare_packets(left, right))

    def part_two_search(self) -> int:
        """
        Determines the indices of the two divider packets and multiplies them together. This method first sorts the
        packets into the `correct` order as stipulated by the problem statement.

        :return: An integer corresponding to the product of the two indices of the divider packets.
        """
        packets = [packet for pair in self.packet_pairs for packet in pair]
        return (1 + sum(1 for p in packets if self.compare_packets(p, [[2]]))) * \
               (2 + sum(1 for p in packets if self.compare_packets(p, [[6]])))

    def solve(self) -> None:
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_search())
        print("Part Two (2):", self.part_two_search())


if __name__ == "__main__":
    distress_signal = DistressSignal()
    distress_signal.solve()
