import heapq

class LinkStateRouter:
    def __init__(self, graph):
        self.graph = graph  # Graph as an adjacency matrix

    def dijkstra(self, start):
        distances = {node: float('inf') for node in range(len(self.graph))}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            curr_dist, curr_node = heapq.heappop(priority_queue)

            # If we've already found a shorter path before, skip
            if curr_dist > distances[curr_node]:
                continue

            for neighbor, weight in enumerate(self.graph[curr_node]):
                # Skip non-connected nodes (weight 0), except self-loops
                if weight == 0 and neighbor != curr_node:
                    continue

                distance = curr_dist + weight

                # If we found a shorter path, update
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def calculate_routes(self):
        return {node: self.dijkstra(node) for node in range(len(self.graph))}


# Example Usage
graph = [
    [0, 2, 0, 1, 0],
    [2, 0, 3, 2, 0],
    [0, 3, 0, 0, 1],
    [1, 2, 0, 0, 4],
    [0, 0, 1, 4, 0]
]

router = LinkStateRouter(graph)
routes = router.calculate_routes()

print("Link State Routing Table:")
for start_node, distances in routes.items():
    print(f"From {start_node}: {distances}")
