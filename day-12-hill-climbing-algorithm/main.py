class HillClimbingAlgorithm:
    """

    """

    def __init__(self) -> None:
        """

        """
        self.length = None
        self.height = None
        self.grid_map = self.construct_data("input.txt")
        self.set_grid_dimensions()
        self.vertices = self.length

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
                grid_map.append([str(row) for row in [*row]])

            return grid_map

    def set_grid_dimensions(self) -> None:
        """
        Sets the length and height of the `grid` for iteration.
        """
        self.length = len(self.grid_map[0])
        self.height = len(self.grid_map)

    def print_solution(self, distance):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", distance[node])

    def min_distance(self, distance, spatial):
        # Initialize minimum distance for next node
        min = 1

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.vertices):
            if ord(distance[v]) < min and ord(spatial[v]) == False:
                min = ord(distance[v])
                min_index = v

        return min_index

    def dijkstra(self, src):

        dist = [1] * self.vertices
        dist[src] = 0
        sptSet = [False] * self.vertices

        for cout in range(self.vertices):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.min_distance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.vertices):
                if (self.grid_map[u][v] > 0 and
                        sptSet[v] == False and
                        dist[v] > dist[u] + self.grid_map[u][v]):
                    dist[v] = dist[u] + self.grid_map[u][v]

        self.print_solution(dist)


if __name__ == "__main__":
    hill_climbing = HillClimbingAlgorithm()
    hill_climbing.dijkstra('S')
