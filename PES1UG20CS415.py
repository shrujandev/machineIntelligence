"""
You can create any other helper funtions.
Do not modify the given functions
"""


def A_star_Traversal(cost, heuristic, start_point, goals):
    """
    Perform A* Traversal and find the optimal path 
    Args:
        cost: cost matrix (list of floats/int)
        heuristic: heuristics for A* (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from A*(list of ints)
    """
    path = []
    # TODO
    return path


def DFS_Traversal(cost, start_point, goals):
    """
    Perform DFS Traversal and find the optimal path 
        cost: cost matrix (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from DFS(list of ints)
    """

    path = []
    visited = []
    stack = []
    print("hello")
    visited.append(start_point)
    path.append(start_point)
    i = 0
    for node in cost[start_point]:
        print(i, "-", node)

        if node > 0:
            stack.append(i)
            print("2", i, "-", node)
        i += 1

    while stack:
        nodeM = stack.pop()
        if nodeM not in visited:
            visited.append(nodeM)
            if nodeM in goals:
                path.append(nodeM)
                break
            else:
                for nodeV in cost[nodeM]:
                    if nodeV not in visited:
                        stack.append(nodeV)
                        path.append(nodeV)

    # TODO
    return path
