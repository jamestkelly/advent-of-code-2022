class CathodeRayTube:
    """
    Main class based solution containing methods for solving Day Nine of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.script = self.construct_data("input.txt")  # Parse the script into memory
        self.ticks = 0  # Initialise the number of ticks
        self.signal_strength = 0  # Set the initial signal strength
        self.crt = ["." for _ in range(40 * 6)]  # Populate the `display` with `empty pixels`
        self.execute_script()  # Simulate the script commands on initialisation

    @staticmethod
    def construct_data(file_name: str) -> list:
        """
        Parses the input script into memory and divides each given command into a function name and the parameter
        provided. In the instance the command is `noop`, then there is no parameter provided and this is the sole
        element at the given index in the list.

        :param file_name: The local file to be parsed into memory
        :return: A list of commands as parsed from the input script
        """
        with open(file_name, 'r') as file_object:
            return [line.strip().split() for line in file_object.readlines()]

    def tick(self, executions: int) -> None:
        """
        Simulates a clock cycle or `tick` of the microcontroller in the problem statement. The method first updates the
        location of the given `pixel` in the simulation and then increments the number of `ticks` performed and updates
        the signal strength.

        :param executions: The value to be executed, i.e., if passed `addx 3` then executions is `3`.
        """
        if self.ticks % 40 in [executions - 1, executions, executions + 1]:  # Update the screen
            self.crt[self.ticks] = "#"

        self.ticks += 1  # Increment the number of `ticks` on the clock cycle

        if self.ticks in range(20, 221, 40):  # Increase the signal strength
            self.signal_strength += executions * self.ticks

    def update_display(self) -> list:
        """
        Iterates through all individual `pixels` contained within the `CRT` or `display` and builds each row of pixels
        that would be displayed to the screen.

        :return: A list containing each row of the `display` (`CRT`).
        """
        return [self.crt[row * 40: 40 + (row * 40)] for row in range(6)]

    def execute_script(self):
        """
        Iterates through all commands parsed from the input script and performs a `switch` based on the command provided
        . For example, in the instance a `noop` execution is provided then only one `tick` or clock cycle is performed.
        Conversely, when an `addx <number>` is provided, then two cycles are performed and the `executions` value is
        increased proportionally to the value in the `<number>` parameter.
        """
        executions = 1  # Initialise executions to `1`
        for line in self.script:
            match line:
                case ['noop']:
                    self.tick(executions)
                case ['addx', number]:
                    self.tick(executions)
                    self.tick(executions)
                    executions += int(number)

    def part_one_search(self) -> int:
        """
        Fetches the calculated signal strength after completion of all `ticks` as per the parsed input script.

        :return: An integer representing the calculated signal strength.
        """
        return self.signal_strength

    def part_two_search(self) -> list:
        """
        Similar to the `part_one_search` method, this method constructs the rows of pixels of the simulated display and
        returns the list of lists containing each row.

        :return: A nested list containing the rows of pixels for the display.
        """
        return self.update_display()

    def solve(self):
        """
        Simple wrapper method to print results to the console.
        """
        display = self.part_two_search()
        print("Part One (1):", self.part_one_search())
        print("Part Two (2):")
        for row in display:
            print(''.join(row))


if __name__ == "__main__":
    cathode_ray = CathodeRayTube()
    cathode_ray.solve()
