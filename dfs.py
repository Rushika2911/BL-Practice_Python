def dfs(graph, start):

    visited = set()
    order = []

    dfs_visit(graph, start, visited, order)

    return order


def dfs_visit(graph, node, visited, order):

    visited.add(node)
    order.append(node)

    for nxt in graph[node]:

        if nxt not in visited:
            dfs_visit(graph, nxt, visited, order)