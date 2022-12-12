from collections import deque


class HillClimbingAlgorithm:
    """
    Main class based solution containing methods for solving Day Twelve of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Init
        """
        self.start_position = ()  # Empty tuple to store the coordinates of the starting position
        self.end_goal = ()  # Empty tuple to store the coordinates of the goal
        self.start_elevations = []  # Empty list to store elevations matching problem statement, e.g., `a` characters
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Surrounding coordinates difference for a given vertex
        self.grid_map = self.construct_data("input.txt")

    def construct_data(self, file_name: str) -> list:
        """
        Constructs the data set provided in `input.txt` into a grid of ASCII characters. Additionally, the starting
        position `S` and end goal position `E` are converted to `a` and `z` respective to their `elevation` as denoted
        by the problem statement.

        :param file_name: The file name to read into memory.
        :return: A list containing the `grid` of ASCII characters representing elevation levels.
        """
        with open(file_name, 'r') as file_object:
            data = [list(row.strip()) for row in file_object.readlines()]

            for x, row in enumerate(data):
                for y, vertex in enumerate(row):
                    match vertex:
                        case "S":
                            self.start_position = (x, y)  # Extract the starting position
                            self.start_elevations.append((x, y))  # Add the position as a start position for Part 2
                            data[x][y] = "a"  # Set the starting position to the lowest elevation level
                        case "E":
                            self.end_goal = (x, y)  # Extract the end goal
                            data[x][y] = "z"  # Set the eng goal as the highest elevation level
                        case "a":
                            self.start_elevations.append((x, y))  # Add the position as a start position for Part 2
                        case _:
                            continue

            return data

    def check_adjacent_vertices(self, elevation_queue: list, column: int, row: int, steps: int) -> list:
        """
        Fetches all adjacent vertices of the dequed vertex at coordinates `(column, row)`. If a given adjacent vertex is
        within the boundaries of the grid's dimensions and is only an increase in `elevation` of `1`, then the vertex is
        appended to the queue to be processed.

        :param elevation_queue: The queue of vertices to visit.
        :param column: The `x` coordinate of the current vertex being processed.
        :param row: The `y` coordinate of the current vertex being processed.
        :param steps: The number of `steps`, i.e., distance from the starting position.
        :return: A `deque` (list-like sequence) containing the vertices to be processed.
        """
        for dx, dy in self.directions:
            if (0 <= column + dx < len(self.grid_map) and
                    0 <= row + dy < len(self.grid_map[0]) and
                    ord(self.grid_map[column + dx][row + dy]) - ord(self.grid_map[column][row]) <= 1
            ):
                elevation_queue.append(((column + dx, row + dy), steps + 1))
        return elevation_queue

    def breadth_first_search(self, multiple_starts: bool = False) -> int:
        """
        Alternative to the standard breadth first search (BFS), this method uses a `set()` to collate an immutable list
        of unique vertices visited rather than a boolean array. This method uses an adjacency list representation of
        graphs.

        :param multiple_starts: Boolean to use a signal position or multiple positions depending on problem statement.
        :return: Either an integer representing the steps required to get from the start position to the end goal, or
            alternatively returns `-1` indicating the method was unable to determine the shortest steps taken, i.e., no
            path to the end goal from the starting position was found.
        """
        visited = set()  # Initialise set to mark unique vertices visited
        if multiple_starts:
            elevation_queue = deque([(start_position, 0) for start_position in self.start_elevations])  # Use all `a`
        else:
            elevation_queue = deque([(start_position, 0) for start_position in [self.start_position]])  # Use `S`

        while elevation_queue:
            position, steps = elevation_queue.popleft()  # Fetch the left-most element from the queue
            if position == self.end_goal:
                return steps  # Successfully found path to end goal
            if position in visited:
                continue
            visited.add(position)
            x, y = position

            elevation_queue = self.check_adjacent_vertices(elevation_queue, x, y, steps)

        return -1  # Fail case

    def part_one_search(self) -> int:
        """
        Determines the fewest steps required to move from the starting position to the end goal to achieve the best
        `signal` on the mountain.

        :return: An integer corresponding to the fewest steps.
        """
        return self.breadth_first_search()

    def part_two_search(self) -> int:
        """
        Determines the fewest steps required to move, starting from any square or vertex in the `grid` with an elevation
        of `a` to the end goal to achieve the best `signal` on the mountain.

        :return: An integer corresponding to the fewest steps.
        """
        return self.breadth_first_search(multiple_starts=True)

    def solve(self) -> None:
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_search())
        print("Part Two (2):", self.part_two_search())


if __name__ == "__main__":
    hill_climbing = HillClimbingAlgorithm()
    hill_climbing.solve()
