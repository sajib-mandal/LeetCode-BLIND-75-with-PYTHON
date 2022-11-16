#  417. Pacific Atlantic Water Flow


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # heights[nr][nc] >= heights[r][c]
        if not heights or not heights[0]:
            return []
        ROWS, COLS = len(heights), len(heights[0])
        pac, alt = set(), set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)
        
        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS - 1, c, alt)
        
        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, alt)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in alt:
                    res.append([r, c])
        return res
        
        
        
        
        
        
        # heights[r][c] < prevHeight
        if not heights or not heights[0]:
            return []
        ROWS, COLS = len(heights), len(heights[0])
        pac, alt = set(), set()
        
        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or r < 0 or c < 0 or 
                 r == ROWS or c == COLS or heights[r][c] < prevHeight):
                return
            visited.add((r, c))
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, alt, heights[r][COLS - 1])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, alt, heights[ROWS -1][c])
            
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in alt:
                    res.append([r, c])
        return res
