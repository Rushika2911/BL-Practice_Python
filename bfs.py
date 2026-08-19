def bidirectional_bfs(graph, start, end):
    if start==end:
        return [start]
    
    q1=[start]
    q2= [end]

    vis1={start}
    vis2={end}

    par1 = {start: None}
    par2 = {end: None}

    while q1 and q2:

        meet = bfs_forward(
            graph,
            q1,
            vis1,
            par1,
            vis2
        )

        if meet is not None:
            return make_path(meet, par1, par2)

        meet = bfs_backward(
            graph,
            q2,
            vis2,
            par2,
            vis1
        )

        if meet is not None:
            return make_path(meet, par1, par2)

    return []


def bfs_forward(graph, q, vis, par, other):

    size = len(q)

    for _ in range(size):

        node = q.pop(0)

        for nxt in graph[node]:

            if nxt not in vis:

                vis.add(nxt)
                par[nxt] = node
                q.append(nxt)

                if nxt in other:
                    return nxt

    return None


def bfs_backward(graph, q, vis, par, other):

    size = len(q)

    for _ in range(size):

        node = q.pop(0)

        for nxt in graph[node]:

            if nxt not in vis:

                vis.add(nxt)
                par[nxt] = node
                q.append(nxt)

                if nxt in other:
                    return nxt

    return None


def make_path(meet, par1, par2):

    path1 = []
    node = meet

    while node is not None:
        path1.append(node)
        node = par1[node]

    path1.reverse()

    path2 = []
    node = par2[meet]

    while node is not None:
        path2.append(node)
        node = par2[node]

    return path1 + path2