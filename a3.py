from queue import PriorityQueue

def a_star_search(graph, start, goal, h):
    """
    A* algorithm to find the shortest path from start to goal.

    graph: dictionary where keys are nodes and values are lists of (neighbor, cost) pairs
    start: starting node
    goal: target node
    h: heuristic function estimating cost from any node to goal

    Returns the shortest path and its total cost.
    """

    # Priority queue to pick the next node to explore based on lowest estimated total cost
    open_set = PriorityQueue()
    open_set.put((0, start))  # (priority, node)

    # Keep track of the cost to reach each node from the start
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0  # cost to reach start is zero

    # To remember the best path: which node we came from to reach current node
    came_from = {}

    while not open_set.empty():
        # Get the node with the lowest total estimated cost (g + h)
        current_f, current = open_set.get()

        # If we reached the goal, build the path to return
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]  # move backward
            path.append(start)
            path.reverse()  # reverse to get path from start to goal
            return path, g_score[goal]

        # Check neighbors of the current node
        for neighbor, cost in graph[current]:
            # Calculate new cost to neighbor through current
            new_cost = g_score[current] + cost

            # If new cost is better, update the path and cost info
            if new_cost < g_score[neighbor]:
                g_score[neighbor] = new_cost
                priority = new_cost + h(neighbor)  # total cost = cost so far + heuristic estimate
                open_set.put((priority, neighbor))
                came_from[neighbor] = current  # remember where we came from

    # If goal was not reached
    return None, float('inf')


# Simple example:

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# A simple guess of distance from each node to goal D (heuristic)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0
}

def h(node):
    return heuristic[node]

path, cost = a_star_search(graph, 'A', 'D', h)

print("Path:", path)
print("Cost:", cost)
