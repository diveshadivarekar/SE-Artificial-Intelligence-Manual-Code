from collections import deque  # Import deque for efficient queue implementation in BFS

# Maze layout:
# 0 represents a path you can walk on
# 1 represents a wall you cannot pass through
maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Maze dimensions
ROWS, COLS = len(maze), len(maze[0])

# Start and end points in the maze
start = (0, 0)            # Top-left corner
end = (ROWS - 1, COLS - 1)  # Bottom-right corner


def print_maze_path(path):
    """
    Print the maze with the path marked.
    The path cells are shown as '*',
    start as 'S', and end as 'E'.
    Walls are printed as '#'.
    """
    # Make a copy of the maze so we don't modify the original
    maze_copy = [row[:] for row in maze]

    for r, c in path:
        if (r, c) == start:
            maze_copy[r][c] = 'S'  # Mark start cell
        elif (r, c) == end:
            maze_copy[r][c] = 'E'  # Mark end cell
        else:
            maze_copy[r][c] = '*'  # Mark the path cells

    # Print the maze row by row
    for row in maze_copy:
        # Print '#' for walls, otherwise print the cell content
        print(' '.join(str(x) if x != 1 else '#' for x in row))
    print()


def neighbors(r, c):
    """
    Generator function that yields all valid neighbors of cell (r, c).
    Neighbors are up, down, left, right cells that are inside the maze boundaries and not walls.
    """
    for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
        if 0 <= nr < ROWS and 0 <= nc < COLS and maze[nr][nc] == 0:
            yield nr, nc


def dfs():
    """
    Depth-First Search algorithm to find a path in the maze.
    Uses a stack (LIFO) to explore as deep as possible.
    Returns the path from start to end if found, else None.
    """
    stack = [start]      # Stack initialized with start cell
    visited = set()      # Keep track of visited cells to avoid loops
    parent = {}          # To store the path, maps each cell to its parent cell

    while stack:
        node = stack.pop()  # Take the last inserted node from the stack
        if node == end:
            break          # If we reached the end, stop searching
        if node in visited:
            continue       # Skip already visited nodes

        visited.add(node)  # Mark current node as visited

        # Visit all neighbors of current node
        for nbr in neighbors(*node):
            if nbr not in visited:
                parent[nbr] = node  # Track where we came from for path reconstruction
                stack.append(nbr)   # Add neighbor to stack for future exploration
    else:
        # If loop exits normally without break, no path was found
        return None
    
    # Reconstruct the path by following parent pointers from end back to start
    path = []
    cur = end
    while cur != start:
        path.append(cur)
        cur = parent[cur]
    path.append(start)
    path.reverse()  # Reverse path so it goes from start to end
    return path


def bfs():
    """
    Breadth-First Search algorithm to find a path in the maze.
    Uses a queue (FIFO) to explore neighbors level by level.
    Returns the shortest path from start to end if found, else None.
    """
    queue = deque([start])   # Queue initialized with start cell
    visited = set([start])   # Mark start as visited immediately
    parent = {}              # To store the path

    while queue:
        node = queue.popleft()  # Take the earliest added node from the queue
        if node == end:
            break              # Stop when end is found

        # Visit all neighbors of current node
        for nbr in neighbors(*node):
            if nbr not in visited:
                visited.add(nbr)  # Mark neighbor as visited when added to queue
                parent[nbr] = node
                queue.append(nbr)
    else:
        # No path found
        return None
    
    # Reconstruct path like in DFS
    path = []
    cur = end
    while cur != start:
        path.append(cur)
        cur = parent[cur]
    path.append(start)
    path.reverse()
    return path


# Print the maze before solving
print("Maze (0=path, #=wall):")
for row in maze:
    print(' '.join(str(x) if x != 1 else '#' for x in row))
print()

print('start =', start)
print('end =', end)
print()

# Solve maze with DFS and print path
path_dfs = dfs()
if path_dfs:
    print("DFS Path:")
    print_maze_path(path_dfs)
else:
    print("No path found by DFS")

# Solve maze with BFS and print path
path_bfs = bfs()
if path_bfs:
    print("BFS Path:")
    print_maze_path(path_bfs)
else:
    print("No path found by BFS")