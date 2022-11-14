# 133. Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        clone = {}
        clone[node] = Node(node.val, [])
        q = collections.deque([node])
        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                clone[cur].neighbors.append(clone[neighbor])
        return clone[node]
    
    
    
        if not node:
            return None
        clone = {}
        clone[node] = Node(node.val, [])
        stack = [node]
        while stack:
            cur = stack.pop()
            for neighbor in cur.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val, [])
                    stack.append(neighbor)
                clone[cur].neighbors.append(clone[neighbor])
        return clone[node]
                
        
        
        
        
        if node == None:
            return None
        copy = {}
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            if cur not in copy:
                copy[cur] = Node(cur.val)
                for n in cur.neighbors:
                    queue.append(n)
        for cur in copy.keys():
            for n in cur.neighbors:
                copy[cur].neighbors.append(copy[n])
        return copy[node]
        
        
        
        
        
        oldToNew = {}
        def dfs(node):
            if not node:
                return None
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) 
