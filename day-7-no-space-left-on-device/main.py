from directory import Directory


class DeviceSpace:
    """
    Main class based solution containing methods for solving Day Seven of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.entries = self.construct_data("input.txt")
        self.root = Directory("/", None, 0, True)
        self.pwd = self.root
        self.read_commands()

    @staticmethod
    def construct_data(file_name: str) -> list:
        """
        Constructs the data set provided in `input.txt` into a list of section assignment pairs.

        :param file_name: The file name to read into memory.
        :return: A list containing the `assignment pairs` to be searched.
        """
        with open(file_name, 'r') as file_object:
            return [line.strip() for line in file_object.readlines()]

    def read_commands(self) -> None:
        """
        This method goes line by line and reads the given string. From there this string is parsed via a `switch` or
        `match` case to determine the action being performed, e.g., 'cd' correlates to changing `directory`. This method
        uses a generic tree structure with `Directory` objects in the place of the traditional nodes. This ad-hoc
        traversal simulates the process used within a Linux file-system to move up and down a tree of directories where
        each file is additionally considered as a directory.
        """
        for entry in self.entries:  # Iterate through all lines
            entry = entry.split()

            match entry[0]:  # Match against the first part of the command, e.g., '$' indicates a command entered
                case "$":
                    if entry[1] == 'cd':  # Verify that it is a change directory not a list directory (`ls`)
                        param = entry[2]  # Fetch the `parameter`, e.g., the directory name, etc.
                        match param:
                            case "/":  # Root directory
                                self.pwd = self.root  # Reset present working directory (`pwd`)
                            case "..":  # Move up a single directory
                                if self.pwd.parent:
                                    self.pwd = self.pwd.parent
                            case _:  # Default case catch-all
                                if param not in self.pwd:  # Directory has not been seen in traverse before
                                    directory = Directory(param, self.pwd, 0, True)  # Create new directory
                                    self.pwd.add_child_directory(directory)  # Add the directory as a child node
                                else:  # Change to that directory
                                    directory = self.pwd[param]
                                self.pwd = directory
                case "dir":  # Case for when directories have been listed, e.g, "dir <directory_name>"
                    directory = Directory(entry[1], self.pwd, 0, True)  # Create a new directory node
                    self.pwd.add_child_directory(directory)  # Add the directory as a child node
                case _:  # Default catch-all for when a file is being listed with a corresponding size
                    self.pwd.add_child_directory(Directory(entry[1], self.pwd, int(entry[0]), False))  # Add file node

    def part_one_search(self) -> int:
        """
        Searches for all directories with a total size of at most 100000 and then calculates the sum of their total
        sizes.

        :return: An integer corresponding to the total size of the directories found.
        """
        total_size = 0  # Initialise a counter to store the sizes found

        for sub_directory in self.root:  # Iterate through all directories
            if sub_directory.has_files and sub_directory.total_size <= 100000:  # Find directory matching conditions
                total_size += sub_directory.total_size  # Add the size of the directory to the `total_size`

        return total_size

    def part_two_search(self) -> int:
        """
        Searches for the smallest directory, that, if deleted, would free up enough space on the filesystem to run the
        update.

        :return: An integer corresponding to the total size of the smallest directory found.
        """
        space = 30000000 - 70000000  # Determine the required space to be found to run the update
        flag = self.root  # Initialise a flag to store the directory of the smallest size

        for sub_directory in self.root:  # Iterate through all directories
            if sub_directory.has_files and self.root.total_size + space < sub_directory.total_size < flag.total_size:
                flag = sub_directory  # Set the current directory found of the smallest size

        return flag.total_size

    def solve(self) -> None:
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_search())
        print("Part Two (2):", self.part_two_search())


if __name__ == "__main__":
    device = DeviceSpace()
    device.solve()
