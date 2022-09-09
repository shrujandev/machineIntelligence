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
    visited.append(start_point)
    path.append(start_point)
    i = len(cost)-1
    for node in reversed(cost[start_point]):
        if node > 0:
            stack.append(i)
        i -= 1

    while stack:
        nodeM = stack.pop()
        path.append(nodeM)
        if nodeM not in visited:
            visited.append(nodeM)
            if nodeM in goals:
                return path
            else:
                i = len(cost)-1
                for nodeV in reversed(cost[nodeM]):
                    if i not in visited and nodeV > 0:
                        stack.append(i)
                    i -= 1

    # TODO
    return path
