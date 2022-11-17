#  261. Graph Valid Tree


def validTree(n, edges):
    if not n:
        return False
    adj = {i: [] for i in range(n)}

    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    visited = set()

    def dfs(i, prev):
        if i in visited:
            return False
        visited.add(i)
        for nei in adj[i]:
            if nei == prev:
                continue
            if not dfs(nei, i):
                return False
        return True
    return dfs(0, -1) and n == len(visited)


print(validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
