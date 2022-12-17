import re


class ProboscideaVolcanium:
    """
    Main class based solution containing methods for solving Day Sixteen of the Advent of Code 2022.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.rooms = {}  # Initialise an empty dictionary to store the rooms in the volcano
        self.flows = {}  # Initialise an empty dictionary to store the flows
        self.values = {}  # Initialise an empty dictionary to store the number of minutes to get to a room from a room
        self.turns = {}  # Initialise an empty dictionary to store the number of turns to get to a room
        self.start_room = "AA"  # Initialise the starting room location
        self.construct_data("input.txt")  # Parse the input data

    def construct_data(self, file_name: str) -> None:
        """
        Parses the data into a series of dictionaries from the input file.

        :param file_name: The file to be read into memory.
        """
        with open(file_name, 'r') as file_object:
            data = [re.split('[\\s=;,]+', line) for line in file_object.readlines()]  # Split the row by spaces
            self.rooms = {line[1]: set(line[10:]) for line in data}  # Construct a dictionary rooms and destinations
            self.flows = {line[1]: int(line[5]) for line in data if int(line[5]) != 0}  # Construct the flow dictionary
            self.values = {entry: 1 << value for value, entry in enumerate(self.flows)}  # Construct value dictionary
            self.turns = {room: {turn: 1 if turn in self.rooms[room] else float('+inf') for turn in self.rooms}
                          for room in self.rooms}  # Construct a default turns dictionary

            for valve in self.turns:  # Iterate through all turns and update the number of turns needed
                for room in self.turns:
                    for num_turns in self.turns:
                        self.turns[room][num_turns] = min(self.turns[room][num_turns],
                                                          self.turns[room][valve] + self.turns[valve][num_turns])

    def visit_room(self, valve: str, max_flow: int, room: int, current_flow: int, result: dict) -> dict:
        """
        Recursive method acting to visit each node (`room`) within the dictionary structures and determine the maximum
        pressure that can be released by turning the valves.

        :param valve: A string corresponding to the name of the room the valve is located.
        :param max_flow: An integer corresponding to the maximum flow achieved.
        :param room: An integer corresponding to the value of the current room.
        :param current_flow: An integer corresponding to the current flow achieved.
        :param result: A dictionary containing the maximum flows achieved.
        :return: A dictionary containing the maximum flows achieved.
        """
        result[room] = max(result.get(room, 0), current_flow)  # Set the current maximum flow achieved as the room

        for new_room in self.flows:  # Iterate through all the rooms and flows
            new_max_flow = max_flow - self.turns[valve][new_room] - 1  # Subtract one `minute`
            
            if self.values[new_room] & room or new_max_flow <= 0:  # Continue searching
                continue
            
            self.visit_room(new_room, new_max_flow, room | self.values[new_room], current_flow + new_max_flow
                            * self.flows[new_room], result)  # Recursive call to update flow search

        return result

    def part_one_search(self) -> int:
        """
        Determines the most pressure that an individual can release within thirty (30) minutes.

        :return: An integer corresponding to the maximum pressure released.
        """
        return max(self.visit_room(self.start_room, 30, 0, 0, {}).values())

    def part_two_search(self) -> int:
        """
        Determines the most pressure than an individual and an elephant would be able to release within twenty-six (26)
        minutes.

        :return: An integer corresponding to the maximum pressure released.
        """
        visited_rooms = self.visit_room(self.start_room, 26, 0, 0, {})
        return max(visit_a + visit_b for path_a, visit_a in visited_rooms.items() for path_b, visit_b
                   in visited_rooms.items() if not path_a & path_b)

    def solve(self) -> None:
        """
        Simple wrapper method to print results to the console.
        """
        print("Part One (1):", self.part_one_search())
        print("Part Two (2):", self.part_two_search())


if __name__ == "__main__":
    proboscidea = ProboscideaVolcanium()
    proboscidea.solve()
