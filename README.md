class DistanceVectorRouter:
    def __init__(self, graph):
        self.graph = graph  # Graph as an adjacency matrix
        self.num_nodes = len(graph)
        self.distances = [[float('inf')] * self.num_nodes for _ in range(self.num_nodes)]

        # Initialize distance to self as 0
        for i in range(self.num_nodes):
            self.distances[i][i] = 0

    def bellman_ford(self):
        # Initial setup based on direct links
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                if self.graph[i][j] != 0:
                    self.distances[i][j] = self.graph[i][j]

        # Updating distances by simulating routers exchanging distances
        for _ in range(self.num_nodes - 1):  # Repeat process for convergence
            for i in range(self.num_nodes):
                for j in range(self.num_nodes):
                    for k in range(self.num_nodes):
                        # Relaxation step
                        if self.distances[i][j] > self.distances[i][k] + self.distances[k][j]:
                            self.distances[i][j] = self.distances[i][k] + self.distances[k][j]

    def calculate_routes(self):
        self.bellman_ford()
        return self.distances


# Example Usage
graph = [
    [0, 2, 0, 1, 0],
    [2, 0, 3, 0, 0],
    [0, 3, 0, 0, 1],
    [1, 0, 0, 0, 4],
    [0, 0, 1, 4, 0]
]

router = DistanceVectorRouter(graph)
routes = router.calculate_routes()

print("Distance Vector Routing Table:")
for start_node, distances in enumerate(routes):
    print(f"From {start_node}: {distances}")              

          remainder = decode_data(received_data, key)

    # Check if there is an error
    if '1' in remainder:
        print("Error detected in received data.")
    else:
        print("No error detected in received data.")
