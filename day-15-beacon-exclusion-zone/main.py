import re


class BeaconExclusionZone:
    """
    Main class based solution containing methods for solving Day Fifteen of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.sensors = {}  # Initialise an empty dictionary to store sensors
        self.beacons = set()  # Initialise an empty set to store beacons
        self.max_y = 2000000  # Set maximum `y` value for part one
        self.max_xy = 4000000  # Set maximum `x` and `y` values for part two
        self.construct_data("input.txt")

    def construct_data(self, file_name: str) -> None:
        """
        Constructs the input data into a format representing the `x` and `y` coordinates of both the sensors and the
        beacons.

        :param file_name: The file to be read into memory.
        """
        with open(file_name, 'r') as file_object:
            data = file_object.readlines()

            for line in data:
                sensor_x, sensor_y, beacon_x, beacon_y = map(int, re.findall(r"=(-?\d+)", line))  # Map the coordinates
                self.sensors[(sensor_x, sensor_y)] = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)  # Add sensors
                self.beacons.add(beacon_y)  # Only need `beacon_y` coordinates

    @staticmethod
    def is_intersection(sensor_a_x: int, sensor_a_y: int, sensor_b_x: int, sensor_b_y: int) -> bool:
        """
        Method to determine whether there is an intersection between the two sensors. In the instance that a match,
        i.e., an intersection is found, then a boolean value is returned.

        :param sensor_a_x: The `x` coordinate of the first sensor to compare.
        :param sensor_a_y: The `y` coordinate of the first sensor to compare.
        :param sensor_b_x: The `x` coordinate of the second sensor to compare.
        :param sensor_b_y: The `y` coordinate of the second sensor to compare.
        :return: A boolean corresponding to whether an intersection was found.
        """
        return (sensor_a_x - 1 <= sensor_b_x <= sensor_a_y + 1 or
                sensor_a_x - 1 <= sensor_b_y <= sensor_a_y + 1 or
                sensor_b_x - 1 <= sensor_a_x <= sensor_b_y + 1 or
                sensor_b_x - 1 <= sensor_a_y <= sensor_b_y + 1)

    @staticmethod
    def convert_point(old_x: int, old_y: int) -> tuple:
        """
        Converts given point to the diagonal position for a given sensor.

        :param old_x: An integer corresponding to the `x` coordinate of the given sensor.
        :param old_y: An integer corresponding to the `y` coordinate of the given sensor.
        :return: A tuple containing the `z` coordinates of the sensor.
        """
        return old_x - old_y, old_x + old_y

    @staticmethod
    def revert_point(new_x: int, new_y: int) -> tuple:
        """
        Reverts the given coordinates to the `x` and `y` coordinates for a beacon.

        :param new_x: An integer corresponding to the new `x` coordinate for the given sensor.
        :param new_y: An integer corresponding to the new `y` coordinate for the given sensor.
        :return: A tuple containing the `x` and `y` coordinates.
        """
        return (new_x + new_y) // 2, (new_x - new_y) // 2

    def union(self, sensor_a: list, sensor_b_x: int, sensor_b_y: int) -> list:
        """
        Method to determine and fetch the union between any two given sensors.

        :param sensor_a: A list containing the `x` and `y` coordinates of a sensor.
        :param sensor_b_x: An integer corresponding to the `x` coordinate of a sensor to compare against.
        :param sensor_b_y: An integer corresponding to the `y` coordinate of a sensor to compare against.
        :return: A list containing the `union` coordinates of the sensors.
        """
        old = []
        united = []

        for sensor_a_x, sensor_a_y in sensor_a:
            if self.is_intersection(sensor_a_x, sensor_a_y, sensor_b_x, sensor_b_y):
                united.append((min(sensor_a_x, sensor_b_x), max(sensor_a_y, sensor_b_y)))
            else:
                old.append((sensor_a_x, sensor_a_y))

        if not united:
            return old + [(sensor_b_x, sensor_b_y)]

        for pair_a, pair_b in united:
            old = self.union(old, pair_a, pair_b)

        return old

    def find_beacon_position(self, sensor_x, sensor_y, manhattan_distance) -> None or tuple:
        """
        Method to determine a potential position for a beacon. In the even that the `y` coordinate of the sensor, minus
        the maximum `y` possible does not exceed the manhattan distance, this method returns `None`.

        :param sensor_x: An integer corresponding to the `x` coordinate of a given sensor.
        :param sensor_y: An integer corresponding to the `y` coordinate of a given sensor.
        :param manhattan_distance: An integer corresponding to the calculated `manhattan distance` of a sensor.
        :return: Either `None` or a `tuple` containing the `x` and `y` coordinates for the beacon.
        """
        if abs(sensor_y - self.max_y) > manhattan_distance:
            return None

        return (sensor_x - (manhattan_distance - abs(sensor_y - self.max_y)),
                sensor_x + (manhattan_distance - abs(sensor_y - self.max_y)))

    def part_one_search(self) -> int:
        """
        Determines, given a maximum `y` value of `2000000`, how many positions cannot contain a beacon.

        :return: An integer corresponding to the number of places a beacon cannot be placed.
        """
        union = []  # Initialise an empty list of unions

        for (sensor_x, sensor_y), manhattan_distance in self.sensors.items():  # Iterate through all sensors
            beacon_position = self.find_beacon_position(sensor_x, sensor_y, manhattan_distance)  # Find the positions

            if beacon_position:
                union = self.union(union, *beacon_position)  # Check if the position is valid

        return union[0][1] - union[0][0] + 1 - sum(beacon_y == self.max_y for beacon_y in self.beacons)

    def part_two_search(self) -> int:
        """
        Given that to find the tuning frequency, the `x` coordinates need to be multiplied by `4000000` and then summed
        with the corresponding `y` coordinate, this method finds the only possible position for the distress beacon and
        returns the tuning frequency.

        :return: An integer corresponding to the tuning frequency of the distress beacon.
        """
        new_points = []

        for (sensor_x, sensor_y), manhattan_distance in self.sensors.items():
            new_points += [self.convert_point(sensor_x, sensor_y + manhattan_distance),
                           self.convert_point(sensor_x - manhattan_distance, sensor_y),
                           self.convert_point(sensor_x + manhattan_distance, sensor_y),
                           self.convert_point(sensor_x, sensor_y - manhattan_distance)]

        new_x_points = sorted(set(new_x for new_x, _ in new_points))
        new_y_points = sorted(set(new_y for _, new_y in new_points))
        new_x = [x + 1 for x, y in zip(new_x_points, new_x_points[1:]) if y - x == 2][0]
        new_y = [y + 1 for y, x in zip(new_y_points, new_y_points[1:]) if x - y == 2][0]
        new_x, new_y = self.revert_point(new_x, new_y)

        return new_x * self.max_xy + new_y

    def solve(self) -> None:
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_search())
        print("Part Two (2):", self.part_two_search())


if __name__ == "__main__":
    beacon = BeaconExclusionZone()
    beacon.solve()
