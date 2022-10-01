# PES1UG20CS415
# SHRUJAN
"""
You can create any other helper funtions.
Do not modify the given functions
"""


from operator import ne


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
    frontier = []
    frontier.append([heuristic[start_point], [start_point]])

    while frontier:
        curCost, pathTaken = frontier.pop(0)
        n = pathTaken[-1]
        curCost -= heuristic[n]
        if n in goals:
            return pathTaken
        path.append(n)

        subTree = []
        for i in range(len(cost[0])):
            if cost[n][i] > 0:
                subTree.append(i)

        for node in subTree:
            newPath = pathTaken + [node]
            newCost = curCost + cost[n][node]+heuristic[node]
            if node not in path and newPath not in [j[1] for j in frontier]:
                frontier.append((newCost, newPath))
                frontier.sort(key=lambda x: (x[0], x[1]))
            elif newPath in [i[1] for i in frontier]:
                index = frontier.index(newPath)
                frontier[index][0] = min(frontier[index][0], newCost)
                frontier.sort(key=lambda x: (x[0], x[1]))

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
