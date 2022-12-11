from monkey import Monkey


class MonkeyBusiness:
    """
    Main class based solution containing methods for solving Day Eleven of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.monkeys = []  # Initialise an empty list to store `Monkey` objects
        self.least_common_multiple = 1  # Initialise the least common multiple (LCM) to `1`

    @staticmethod
    def construct_data(file_name: str) -> list:
        """
        Constructs the dataset provided in the given input file into a list of `Monkey` objects as per the dataclass
        contained in `monkey.py`.

        :param file_name: The given file to be read into memory.
        :return: A list of `Monkey` objects.
        """
        with open(file_name, 'r') as file_object:
            monkeys = []  # Initialise an empty list to store `Monkey` objects
            counter = 1  # Initialise a counter to track lines seen
            for line in file_object.readlines():
                line = line.rstrip()  # Remove all trailing white-spaces
                match counter % 7:  # Match action to given line seen
                    case 1:  # First line contains the monkey's ID number
                        monkeys.append(Monkey())  # Initialise a new monkey object
                    case 2:  # Second line contains the monkey's inventory
                        monkeys[-1].items = line[18:].split(", ")  # Take the list item worry levels
                        monkeys[-1].items = [int(x) for x in monkeys[-1].items]  # Convert to integers
                    case 3:  # Third line contains the `operation` performed on an item in inventory
                        monkeys[-1].operation = line[19:]  # Fetch the operation string
                        monkeys[-1].operation = monkeys[-1].operation.replace("old", "monkey.items[0]")
                    case 4:  # Fourth line contains the number to divide by for the `test`
                        monkeys[-1].divisible_by = int(line.split(" ")[-1])
                    case 5:  # Fifth line contains the number corresponding to the monkey to give the item to on success
                        monkeys[-1].throws[0] = int(line[-1])
                    case 6:  # Sixth line contains the number corresponding to the monkey to give the item to on failure
                        monkeys[-1].throws[1] = int(line[-1])
                counter += 1

        return monkeys

    def generate_least_common_multiple(self) -> None:
        """
        The least common multiple is defined as the smallest multiple that two or more numbers have in common. This
        method works to set the least common multiple or `LCM`.
        """
        self.least_common_multiple = 1  # Reset least common multiple to `1`
        for monkey in self.monkeys:
            self.least_common_multiple *= monkey.divisible_by

    def simulate_monkey_business(self, rounds: int, reduce_worry: bool = True) -> int:
        """
        Simulates the `rounds` in which the monkeys are inspecting and then passing the items. This method
        processes all turns for a monkey as per the problem statement and then finds the product of the amount of
        `worry` generated by the two most active monkeys.

        :param rounds: The number of `rounds` the monkeys will inspect the items over.
        :param reduce_worry: Boolean representing whether the `worry` is reduced.
        :return: An integer representing the level of `monkey business` after the given number of rounds.
        """
        self.monkeys = self.construct_data("input.txt")  # Generate the monkey data objects
        for _ in range(rounds):
            for monkey in self.monkeys:
                for item in range(0, len(monkey.items)):  # Iterate through all items in the Monkey's inventory
                    monkey.inspections += 1  # Increment the inspections
                    monkey.items[0] = eval(monkey.operation)  # Evaluate the `operation` is an expression
                    if reduce_worry:
                        monkey.items[0] = monkey.items[0] // 3  # Divide by `3` and round down to the nearest integer
                    else:
                        monkey.items[0] = monkey.items[0] % self.least_common_multiple  # Modulo by `LCM`
                    if monkey.items[0] % monkey.divisible_by == 0:  # Perform the `test`
                        self.monkeys[monkey.throws[0]].items.append(monkey.items.pop(0))  # `Throw` to given monkey
                    else:
                        self.monkeys[monkey.throws[1]].items.append(monkey.items.pop(0))  # `Throw` to given monkey

        monkey_inspections = [int(self.monkeys[i].inspections) for i in range(len(self.monkeys))]
        monkey_inspections.sort()  # Sort the array of monkey inspections
        return monkey_inspections[-1] * monkey_inspections[-2]  # Return the product of the top two monkeys

    def part_one_search(self) -> int:
        """
        Determines the level of monkey business after twenty (20) rounds of stuff-slinging simian shenanigans.

        :return: An integer corresponding to the level of monkey business.
        """
        return self.simulate_monkey_business(20, True)

    def part_two_search(self) -> int:
        """
        Given that a monkey's inspection didn't damage an item no longer causes the worry level to be divided by three.
        This method determines the level of monkey business after ten thousand (10000) rounds of stuff-slinging simian
        shenanigans.

        :return: An integer corresponding to the level of monkey business.
        """
        self.generate_least_common_multiple()
        return self.simulate_monkey_business(10000, False)

    def solve(self) -> None:
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_search())
        print("Part Two (2):", self.part_two_search())


if __name__ == "__main__":
    monkey_business = MonkeyBusiness()
    monkey_business.solve()