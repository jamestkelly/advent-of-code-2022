class RopeBridge:
    """
    Main class based solution containing methods for solving Day Nine of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.moves = self.construct_data("input.txt")
        self.directions = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}

    @staticmethod
    def parse_move(move: str) -> tuple:
        """
        Parses a given string containing the `move` for the `rope` to take. This method splits to string into two parts,
        the direction and the `magnitude` or distance that the rope will move in the given direction.

        :param move: The string containing the direction and magnitude for the rope to move.
        :return: A tuple containing the direction and magnitude for the rope to move.
        """
        return move.split(" ")[0], int(move.split(" ")[1])

    @staticmethod
    def get_difference(head_pos, tail_pos) -> int:
        """
        Determines the absolute difference between the `x` and `y` coordinates via the in-built `abs` method.

        :param head_pos: A list containing the `x` and `y` coordinates of the `head`.
        :param tail_pos: A list containing the `x` and `y` coordinates of the `tail`.
        :return: An integer representing difference between the coordinates.
        """
        return abs(head_pos[0] - tail_pos[0]) + abs(head_pos[1] - tail_pos[1])

    def update_tail_position(self, head_pos, tail_pos) -> list:
        """
        Updates the position of the `tail` within the `grid` to reflect changes made to the `head` of the `rope`. This
        is simply a series of nested conditionals to verify the location of the `tail` in relation to the `head`.

        :param head_pos: A list containing the `x` and `y` coordinates of the `head`.
        :param tail_pos: A list containing the `x` and `y` coordinates of the `tail`.
        :return: A list containing the updated `x` and `y` coordinates of the `tail`.
        """
        if abs(head_pos[0] - tail_pos[0]) == 2 and head_pos[1] == tail_pos[1]:
            if head_pos[0] > tail_pos[0]:
                tail_pos[0] += 1
            else:
                tail_pos[0] -= 1

        elif abs(head_pos[1] - tail_pos[1]) == 2 and head_pos[0] == tail_pos[0]:
            if head_pos[1] > tail_pos[1]:
                tail_pos[1] += 1
            else:
                tail_pos[1] -= 1

        elif head_pos[0] != tail_pos[0] and head_pos[1] != tail_pos[1]:
            if self.get_difference(head_pos, tail_pos) > 2:
                if head_pos[0] > tail_pos[0]:
                    tail_pos[0] += 1
                else:
                    tail_pos[0] -= 1
                if head_pos[1] > tail_pos[1]:
                    tail_pos[1] += 1
                else:
                    tail_pos[1] -= 1

        return tail_pos

    @staticmethod
    def construct_data(file_name: str) -> list:
        """
        Constructs the data set provided in `input.txt` into a list of direction and magnitudes.

        :param file_name: The file name to read into memory.
        :return: A list containing the `moves` of direction and magnitudes for the rope to move.
        """
        with open(file_name, 'r') as file_object:
            return [move.strip() for move in file_object.readlines()]

    def part_one_search(self) -> int:
        """
        Searches the list of instructions and simulates the movements of the `rope` to determine how many positions the
        tail of the rope visits at least once.

        :return: An integer representing the length of a list of positions (without duplicates) reached by the tail.
        """
        head_pos = [0, 0]
        tail_pos = [0, 0]
        result = ['0 0']

        for move in self.moves:
            move = self.parse_move(move)
            direction = self.directions[move[0]]

            for i in range(0, move[1]):
                head_pos[0] += direction[0]
                head_pos[1] += direction[1]
                tail_pos = self.update_tail_position(head_pos, tail_pos)
                result.append(' '.join([str(position) for position in tail_pos]))

        return len(set(result))  # Remove duplicates and find the length of positions reached by the `tail`

    def part_two_search(self) -> int:
        """
        Similar to `part_one_search`, this method searches the list of instructions, albeit with a rope with ten (10)
        `knots`. The method loops through all moves and updates each position of the `rope` and builds a list of
        positions that the rope has visited. This list is then converted to a set to remove duplicates and the length
        of the list is returned.

        :return: An integer representing the number of positions the tail visited.
        """
        result = ['0 0']
        rope = [[0, 0] for _ in range(10)]  # Initialise a rope with 10 `knots`

        for move in self.moves:
            move = self.parse_move(move)
            direction = self.directions[move[0]]

            for i in range(0, move[1]):
                rope[0][0] += direction[0]
                rope[0][1] += direction[1]

                for j in range(1, 10):
                    self.update_tail_position(rope[j - 1], rope[j])

                result.append(' '.join([str(position) for position in rope[9]]))

        return len(set(result))  # Remove duplicates and find the length of positions reached by the `tail`

    def solve(self):
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_search())
        print("Part Two (2):", self.part_two_search())


if __name__ == "__main__":
    rope_bridge = RopeBridge()
    rope_bridge.solve()
