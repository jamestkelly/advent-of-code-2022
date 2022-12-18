from rockstats import RockStats


class PyroclasticFlow:
    """
    Main class based solution containing methods for solving Day Seventeen of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.data = self.construct_data("input.txt")
        self.rocks = RockStats()
        self.peaks = [0, 0, 0, 0, 0, 0, 0]  # Initialise the peaks to 0

    @staticmethod
    def construct_data(file_name: str) -> list:
        """
        Reads data from an input file into memory and converts the string into individual characters.

        :param file_name: A string containing the name of the file to be read into memory.
        :return: A list containing the parsed chars.
        """
        with open(file_name, 'r') as file_object:
            data = [row.strip() for row in file_object.readlines()]
            return [*data[0]]

    @staticmethod
    def fetch_position(name: str, height: int) -> list:
        """
        Match-case method wrapper to parse a given shape name against the updated details for the object, i.e., the
        list of tuples is incremented and then returned correlating to the change differing by the shape of the given
        `rock`.

        :param height: An integer corresponding to the height to increase by.
        :param name: A string containing the name of the object to be matched against.
        :return: A list containing the tuples of the dimensions for the given rock.
        """
        match name:
            case "horizontal-line":
                return [(height + 3, 2), (height + 3, 3), (height + 3, 4), (height + 3, 5)]
            case "vertical-line":
                return [(height + 3, 2), (height + 4, 2), (height + 5, 2), (height + 6, 2)]
            case "l-shape":
                return [(height + 3, 2), (height + 3, 3), (height + 3, 4), (height + 4, 4), (height + 5, 4)]
            case "block":
                return [(height + 3, 2), (height + 3, 3), (height + 4, 2), (height + 4, 3)]
            case "cross":
                return [(height + 3, 3), (height + 4, 2), (height + 4, 3), (height + 4, 4), (height + 5, 3)]

    @staticmethod
    def simulate_rock_fall(positions: list, state: list) -> tuple:
        """
        Method to simulate a rock falling.

        :param positions: A list containing the current coordinates of the rocks.
        :param state: A list containing the current `state` or series of positions of the rocks.
        :return: A tuple containing the updated positions and a boolean corresponding to whether the rock can fall or
            not.
        """
        new_positions = []

        for position in positions:
            if position[0] == 0 or state[position[0] - 1][position[1]] != 0:
                return None, False
            else:
                new_positions.append((position[0] - 1, position[1]))

        return new_positions, True

    @staticmethod
    def simulate_move(move: str, positions: list, state: list) -> list:
        """
        Simulates a given move in the tetris-like game whereby `rock` objects fall and their respective positions within
        the boundaries of the grid, i.e., display, are updated.
        
        :param move: A string corresponding to the type of move, e.g., either of the "<" or ">" characters.
        :param positions: A list containing the current positions held by the `rock` objects.
        :param state: A list containing the current `state` or series of positions of the rocks.
        :return: A list containing the updated positions held by the `rock` objects.
        """
        new_positions = []

        match move:
            case "<":
                for position in positions:
                    if position[1] == 0 or state[position[0]][position[1] - 1] != 0:
                        return positions
                    new_positions.append((position[0], position[1] - 1))

                return new_positions
            case ">":
                for position in positions:
                    if position[1] == 6 or state[position[0]][position[1] + 1] != 0:
                        return positions
                    new_positions.append((position[0], position[1] + 1))

                return new_positions

    def build_state(self):
        """
        Method to construct and initialise a new empty `state` list of lists containing seven (7) zeroes.
        
        :return: A list of lists containing zeroes (0s).
        """
        return [list(self.peaks) for _ in range(4)]

    def part_one_search(self) -> int:
        """
        Determines how tall the tower of rocks will get after two thousand and twenty-two (2022) rocks have stopped
        falling.
        
        :return: An integer corresponding to how many units tall the tower of rocks will be.
        """
        state = self.build_state()
        peak = -1
        num_moves = 0

        for rock in range(self.rocks.max_moves[0]):
            new_rock = list(self.rocks.stats)[rock % 5]
            new_position = self.fetch_position(new_rock, peak + 1)

            for _ in range(self.rocks.stats[new_rock]["height"]):
                state.append(list(self.peaks))

            while True:
                if num_moves >= len(self.data):
                    num_moves -= len(self.data)

                new_position = self.simulate_move(self.data[num_moves], new_position, state)
                num_moves += 1
                fallen, can_fall = self.simulate_rock_fall(new_position, state)

                if not can_fall:
                    for position in new_position:
                        state[position[0]][position[1]] = 1
                        if position[0] > peak:
                            peak = position[0]
                    break

                new_position = fallen

        return peak + 1

    def part_two_search(self) -> int:
        """
        Determines how tall the tower of rocks will get after 1000000000000 rocks have stopped falling.

        :return: An integer corresponding to how many units tall the tower of rocks will be.
        """
        state = self.build_state()
        peak = -1
        num_moves = 0
        visited = {}
        heights = {}

        for rock in range(self.rocks.max_moves[1]):
            new_rock = list(self.rocks.stats)[rock % 5]
            new_position = self.fetch_position(new_rock, peak + 1)

            for _ in range(self.rocks.stats[new_rock]["height"]):
                state.append([0, 0, 0, 0, 0, 0, 0])

            while True:
                if num_moves >= len(self.data):
                    num_moves -= len(self.data)

                new_position = self.simulate_move(self.data[num_moves], new_position, state)
                num_moves += 1
                fallen, can_fall = self.simulate_rock_fall(new_position, state)

                if not can_fall:
                    peak_old = peak

                    for position in new_position:
                        state[position[0]][position[1]] = 1

                        if position[0] > peak:
                            peak = position[0]

                    max_change = peak - peak_old

                    for index in range(7):
                        self.peaks[index] -= max_change

                    for position in new_position:
                        this_peak = position[0] - peak
                        self.peaks[position[1]] = max(self.peaks[position[1]], this_peak)

                    break

                new_position = fallen

            heights[rock] = peak
            key = (tuple(self.peaks), num_moves, rock % 5)

            if key in visited.keys():
                if visited[key] != 0:
                    height_difference = peak - heights[visited[key]]
                    goal = self.rocks.max_moves[1] - visited[key]  # Update how many more rocks need to fall
                    leftover_height = heights[visited[key] + (goal % (rock - visited[key]))] - heights[visited[key]]

                    return heights[visited[key]] + leftover_height + ((goal // (rock - visited[key]))
                                                                      * height_difference)

            visited[key] = rock

        return peak + 1

    def solve(self):
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_search())
        print("Part Two (2):", self.part_two_search())


if __name__ == "__main__":
    pyro = PyroclasticFlow()
    pyro.solve()
