#  200. Number of Islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if ((r, c) in visited or r < 0 or c < 0 or 
                 r == ROWS or c == COLS or grid[r][c] == "0"):
                return 0
            visited.add((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)   
        ilands = 0   
        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) not in visited and grid[r][c] == "1"):
                    dfs(r, c)
                    ilands += 1
        return ilands
        
        
        
        # BFS
        if not grid or not grid[0]:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        (nr, nc) not in visited and grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        visited.add((nr, nc))   
        count = 0       
        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) not in visited and grid[r][c] == "1"):
                    bfs(r, c)
                    count += 1
        return count
    
    
    
        # DFS ITERATIVE
        if not grid or not grid[0]:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()
        def bfs(r, c):
            stack = []
            stack.append((r, c))
            visited.add((r, c))
            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        (nr, nc) not in visited and grid[nr][nc] == "1"):
                        stack.append((nr, nc))
                        visited.add((nr, nc))   
        count = 0       
        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) not in visited and grid[r][c] == "1"):
                    bfs(r, c)
                    count += 1
        return count
        
        
        
        
        r, c = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        count = 0
        def findIsland(x, y):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < r and 0 <= ny < c and grid[nx][ny] == "1" and 
                    (nx, ny) not in visited):
                    visited.add((nx, ny))
                    findIsland(nx, ny)
        for x in range(r):
            for y in range(c):
                if grid[x][y] == "1" and (x, y) not in visited:
                    count += 1
                    visited.add((x, y))
                    findIsland(x, y)
        return count
