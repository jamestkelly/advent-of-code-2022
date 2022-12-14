class RegolithReservoir:
    """
    Main class based solution containing methods for solving Day Eleven of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.point = (500, 0)  # Initialise the point from which the sand is pouring
        self.cave = {}  # Initialise an empty cave dictionary
        self.boundary = None  # Initialise a boundary variable
        self.floor = self.result = 0  # Set the floor and the count of units of sand that rest
        self.vertical = []

    def construct_data(self, file_name: str) -> None:
        """
        Constructs the input data into a format representing the two-dimensional vertical slices of the cave.
        """
        cave = {}  # Initialise an empty cave dictionary
        with open(file_name, "r") as file_object:
            data = file_object.read()

            for line in data.splitlines():  # Iterate through all lines
                raw_paths = line.split(" -> ")  # Split the line based on the data delimiters
                paths = []  # Initialise a cleaned paths list

                for path in raw_paths:  # Iterate through all raw paths
                    paths.append(tuple(map(int, path.split(","))))  # Add the cleaned path as a tuple

                right, down = paths.pop(0)  # Pop the first element from the list
                cave[right, down] = "#"  # Draw the `rock`

                for right_new, down_new in paths:  # Iterate through all remaining points onwards from the rock
                    distance_right, distance_down = right_new - right, down_new - down  # Find the distance
                    if distance_right != 0:
                        distance_right = distance_right // abs(distance_right)  # Divide and round down
                    if distance_down != 0:
                        distance_down = distance_down // abs(distance_down)  # Divide and round down

                    while right != right_new or down != down_new:
                        right += distance_right  # Increment the distance right
                        down += distance_down  # Increment the distance down
                        cave[right, down] = '#'  # Draw the `rock`

        self.cave = cave  # Set the drawn cave

    def set_variables(self) -> None:
        """
        Sets variables to their initial state for each execution, e.g., after completion of part one, the cave needs to
        be reset to its original state.
        """
        self.construct_data("input.txt")
        self.boundary = max(down for right, down in self.cave.keys())
        self.result = 0
        self.floor = self.boundary + 2
        self.result = 0
        self.vertical = [self.point[0] - self.floor - 2, self.point[0] + self.floor + 3]

    def simulate_falling_sand(self, right, down, boundary) -> bool:
        """
        Series of conditional statements to increment the path as the units of sand `fall`. A unit of sand will always
        fall down a single step if possible. If the tile immediately below is blocked (by rock or sand), the unit of
        sand attempts to instead move diagonally one step down and to the left. If that tile is blocked, the unit of
        sand attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as it is able
        to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations
        are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of sand is created
        back at the source. When a unit of sand achieves a `rest` state, a "o" is drawn.

        :param right: An integer representing the distance to the right.
        :param down: An integer representing the distance to the down.
        :param boundary: An integer representing the limit of the cave, i.e., the abyss.
        :return: A boolean representing whether the sand has reached a `rest` state.
        """
        while (right, down) not in self.cave:
            if down > boundary:  # End of cave reached
                return False
            if (right, down + 1) not in self.cave:  # Go directly down
                down += 1
                continue
            if (right - 1, down + 1) not in self.cave:  # Go diagonal
                right -= 1
                down += 1
                continue
            if (right + 1, down + 1) not in self.cave:  # Go diagonal
                right += 1
                down += 1
                continue

            self.cave[right, down] = "o"  # Sand has achieved `rest` state
            return True

    def part_one_search(self) -> int:
        """
        Method to simulate the falling sand and determine how many units of sand come to rest before the sand starts
        flowing to the `boundary`, i.e., the abyss below the cave.

        :return: An integer representing how many units of sand achieve rest.
        """
        self.set_variables()  # Set the variables

        while self.simulate_falling_sand(self.point[0], self.point[1], self.boundary):
            self.result += 1

        return self.result

    def part_two_search(self):
        """
        Similar to `part_one_search()`, this method simulates the falling sand, albeit until the source of the sand
        becomes blocked. This method draws upon the change in the problem statement whereby instead of an abyss or
        boundary, there is a `floor` to the cave.

        :return: An integer corresponding to the number of units of sand come to `rest`.
        """
        self.set_variables()  # Reset the variables

        for i in range(self.vertical[0], self.vertical[1]):
            self.cave[i, self.floor] = "#"

        while self.cave.get(self.point) is None:
            assert self.simulate_falling_sand(self.point[0], self.point[1], self.floor)
            self.result += 1

        return self.result

    def solve(self):
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_search())
        print("Part Two (2):", self.part_two_search())


if __name__ == "__main__":
    regolith_reservoir = RegolithReservoir()
    regolith_reservoir.solve()
