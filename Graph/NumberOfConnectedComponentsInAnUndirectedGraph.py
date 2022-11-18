#   323. Number of Connected Components in an Undirected Graph


# import collections

def numConnected(n, edges):
    # if not n:
    #     return 0
    # adj = {i: [] for i in range(n)}
    #
    # for n1, n2 in edges:
    #     adj[n1].append(n2)
    #     adj[n2].append(n1)
    #
    # visited = set()
    #
    # def dfs(i):
    #     if i in visited:
    #         return
    #     visited.add(i)
    #     count = 1
    #     for nei in adj[i]:
    #         if not dfs(nei):
    #             count += 1
    #         dfs(nei)
    #     return count
    #
    # return dfs(0)
    
    
    # Queue
    adj = {i: [] for i in range(n)}
    for source, target in edges:
        adj[source].append(target)
        adj[target].append(source)
    count = 0
    visited = set()
    q = collections.deque()
    for x in range(n):
        if x in visited:
            continue
        q.append(x)
        while q:
            source = q.popleft()
            if source in visited:
                continue
            visited.add(source)
            for target in adj[source]:
                q.append(target)
        count += 1
    return count
    
    
    
    # Stack
    adj = {i: [] for i in range(n)}
    for source, target in edges:
        adj[source].append(target)
        adj[target].append(source)
    count = 0
    visited = set()
    stack = []
    for x in range(n):
        if x in visited:
            continue
        stack.append(x)
        while stack:
            source = stack.pop()
            if source in visited:
                continue
            visited.add(source)
            for target in adj[source]:
                stack.append(target)
        count += 1
    return count


print(numConnected(5, [[0, 1], [1, 2], [3, 4]]))
