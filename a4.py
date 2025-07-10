from collections import deque

def ac3(domains, neighbors):
    """
    AC-3 algorithm for constraint propagation.
    It enforces arc consistency between variables (regions).
    """
    queue = deque()
    # Initialize queue with all arcs (variable pairs)
    for var in neighbors:
        for neighbor in neighbors[var]:
            queue.append((var, neighbor))

    while queue:
        xi, xj = queue.popleft()
        if remove_inconsistent_values(xi, xj, domains):
            # If domain of xi was reduced, add arcs (xk, xi) back to queue
            if len(domains[xi]) == 0:
                return False  # Failure, no legal values left
            for xk in neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True

def remove_inconsistent_values(xi, xj, domains):
    """
    Remove values from xi's domain that have no compatible value in xj's domain.
    """
    removed = False
    for x in set(domains[xi]):  # Use set to avoid modifying during iteration
        # If no value y in xj's domain allows (x != y), remove x from xi's domain
        if all(x == y for y in domains[xj]):
            domains[xi].remove(x)
            removed = True
    return removed

def backtrack(assignment, domains, neighbors):
    """
    Backtracking search to assign colors to all regions.
    """
    # If all variables assigned, return assignment
    if len(assignment) == len(domains):
        return assignment

    # Select unassigned variable with smallest domain (MRV heuristic)
    unassigned_vars = [v for v in domains if v not in assignment]
    var = min(unassigned_vars, key=lambda v: len(domains[v]))

    for value in domains[var]:
        # Check if value consistent with assignment (no neighbor has same color)
        if all(assignment.get(neigh) != value for neigh in neighbors[var]):
            assignment[var] = value

            # Make a copy of domains for constraint propagation
            local_domains = {v: list(domains[v]) for v in domains}
            local_domains[var] = [value]

            # Propagate constraints
            if ac3(local_domains, neighbors):
                result = backtrack(assignment, local_domains, neighbors)
                if result:
                    return result

            # If failure, remove assignment and try next value
            assignment.pop(var)

    return None

# Example: Map coloring for Australia
def main():
    # Variables = regions
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

    # Domains = possible colors for each region
    colors = ['Red', 'Green', 'Blue']
    domains = {var: colors[:] for var in variables}

    # Neighbors (constraints): adjacent regions must have different colors
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []  # Tasmania has no neighbors
    }

    assignment = {}
    solution = backtrack(assignment, domains, neighbors)

    if solution:
        print("Solution found:")
        for region in sorted(solution):
            print(f"{region}: {solution[region]}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
