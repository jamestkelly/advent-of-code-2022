class BoilingBoulders:
    """
    Main class based solution containing methods for solving Day Seventeen of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.data = self.construct_data("input.txt")

    @staticmethod
    def construct_data(file_name: str) -> set:
        """
        Reads data from an input file into memory and converts the string into indexividual characters.

        :param file_name: A string containing the name of the file to be read into memory.
        :return: A list containing the parsed chars.
        """
        with open(file_name, 'r') as file_object:
            data = [line.strip() for line in file_object if line.strip()]
            return set(map(eval, data))

    @staticmethod
    def find_adjacent(point: tuple) -> tuple:
        """
        Method to return a generator object containing a tuple of coordinates, e.g., points to iterate over.

        :param point: A tuple containing the x, y, and z coordinates for a given cube.
        :return: An iterable tuple containig the coordinates.
        """
        for axis in range(3):
            for coordinate in (-1, 1):
                points = list(point)
                points[axis] += coordinate

                yield tuple(points)

    def part_one_search(self):
        """
        Method to determine the total surface area for a scanned lava droplet. This method counts up all sides that are
        not connected to another `cube` object and calculates the total surface area.

        :return: An integer corresponding to the surface area of the scanned lava droplet.
        """
        return sum(1 for point in self.data for points in self.find_adjacent(point) if points not in self.data)

    def part_two_search(self):
        """
        This method is similar to `part_one_search()`, however, instead this method considers only cubes that can be
        reached by the water and steam as the lava droplet tumbles into the pond. The steam will expand to reach as much
        as possible, completely displacing any air on the outside of the lava droplet but never expand diagonally. Given
        this information, this method calculates the exterior surface area of the scanned lava droplet.

        :return: An integer corresponding to the exterior surface area of the scanned lava droplet.
        """
        cube_min = tuple(min(point[axis] for point in self.data) - 1 for axis in range(3))
        cube_max = tuple(max(point[axis] for point in self.data) + 1 for axis in range(3))
        stack = [cube_min]
        visited = set()
        exterior_surface_area = 0

        while stack:
            point = stack.pop()

            if point in visited:
                continue

            visited.add(point)

            for new_point in self.find_adjacent(point):
                if new_point in self.data:
                    exterior_surface_area += 1

                if (new_point not in self.data and new_point not in visited
                        and all(x <= y <= z for x, y, z in zip(cube_min, new_point, cube_max))):
                    stack.append(new_point)

        return exterior_surface_area

    def solve(self):
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_search())
        print("Part Two (2):", self.part_two_search())


if __name__ == "__main__":
    boil = BoilingBoulders()
    boil.solve()
