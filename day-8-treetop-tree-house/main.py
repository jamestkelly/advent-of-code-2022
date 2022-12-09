class TreeHouse:
    """
    Main class based solution containing methods for solving Day Eight of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.length = None
        self.height = None
        self.grid_map = self.construct_data("input.txt")
        self.set_grid_dimensions()

    @staticmethod
    def construct_data(file_name: str) -> list:
        """
        Constructs the data set provided in `input.txt` into a list of section assignment pairs.

        :param file_name: The file name to read into memory.
        :return: A list containing the `assignment pairs` to be searched.
        """
        with open(file_name, 'r') as file_object:
            data = [row.strip() for row in file_object.readlines()]
            grid_map = []

            for row in data:
                grid_map.append([eval(row) for row in [*row]])

            return grid_map

    def set_grid_dimensions(self) -> None:
        """
        Sets the length and height of the `grid` for iteration.
        """
        self.length = len(self.grid_map[0])
        self.height = len(self.grid_map)

    def is_boundary(self, row, column) -> bool:
        """
        This method determines whether the current `pointer` location within the `grid` of tree heights is on the edge
        or boundary of the map.

        :return: A boolean true or false.
        """
        return row == 0 or row == self.height - 1 or column == 0 or column == self.length - 1

    def is_taller(self, row: int, column: int, tree: int) -> bool:
        """
        This method determines whether the supplied `tree` parameter is of a greater or equal value
        to the provided tree in the provided `row` and `column` of the `grid`.

        :return: A boolean true or false.
        """
        return self.grid_map[row][column] >= tree

    def part_one_search(self) -> int:
        """
        Searches the `grid` for all trees and determines their visibility by comparing the `height` of a given tree
        against all surrounding trees.

        :return: An integer corresponding to the total number of trees visible from outside the grid.
        """
        visible_trees = 0  # Counter for the number of visible trees in the grid
        for row in range(self.height):
            for column in range(self.length):
                if self.is_boundary(row, column):
                    visible_trees += 1
                    continue

                tree = self.grid_map[row][column]

                for k in range(0, row):  # Check north
                    if self.is_taller(k, column, tree):
                        break
                else:
                    visible_trees += 1
                    continue

                for k in range(row + 1, self.height):  # Check south
                    if self.is_taller(k, column, tree):
                        break
                else:
                    visible_trees += 1
                    continue

                for k in range(0, column):  # Check east
                    if self.is_taller(row, k, tree):
                        break
                else:
                    visible_trees += 1
                    continue

                for k in range(column + 1, self.length):  # Check west
                    if self.is_taller(row, k, tree):
                        break
                else:
                    visible_trees += 1
                    continue

        return visible_trees

    def part_two_search(self) -> int:
        """
        Searches for the highest `scenic score` possible for any given `tree` within the `grid` map of trees. A tree's
        `scenic score` is found by multiplying together its viewing distance in each of the four cardinal directions,
        e.g., `(north * south * east * west)`.

        :return: An integer corresponding to the maximum scenic score possible for any tree.
        """
        scenic_score = 0  # Initialise the maximum scenic score

        for row in range(self.height):  # Iterate over all the trees in the grid.
            for column in range(self.length):
                tree = self.grid_map[row][column]  # Set the tree
                score = 1  # Initialise a score tracker
                counter = 0  # Initialise a counter variable

                for k in reversed(range(0, row)):  # Check north
                    counter += 1
                    if self.grid_map[k][column] >= tree:
                        break

                score *= counter  # Multiply the score by the counter
                counter = 0  # Reset the counter

                for k in range(row + 1, self.height):  # Check south
                    counter += 1
                    if self.grid_map[k][column] >= tree:
                        break

                score *= counter  # Multiply the score by the counter
                counter = 0  # Reset the counter

                for n in reversed(range(0, column)):  # Check east
                    counter += 1
                    if self.grid_map[row][n] >= tree:
                        break

                score *= counter  # Multiply the score by the counter
                counter = 0  # Reset the counter

                for n in range(column + 1, self.length):  # Check west
                    counter += 1
                    if self.grid_map[row][n] >= tree:
                        break

                score *= counter  # Multiply the score by the counter
                scenic_score = max(scenic_score, score)  # Update the maximum scenic score

        return scenic_score

    def solve(self) -> None:
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_search())
        print("Part Two (2):", self.part_two_search())


if __name__ == "__main__":
    tree_house = TreeHouse()
    tree_house.solve()
