"""
0: already disconnected
1: disconnected after removing one land cell
2: requires removing two land cells
"""

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def count_islands():
            visited = set()

            def dfs(x, y):
                stack = [(x, y)]
                while stack:
                    x, y = stack.pop()
                    for nx, ny in [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]:
                        if (
                            0 <= nx < m and 0 <= ny < n
                            and grid[nx][ny] == 1
                            and (nx, ny) not in visited
                        ):
                            visited.add((nx, ny))
                            stack.append((nx, ny))
            
            islands = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] and (i, j) not in visited:
                        islands += 1
                        visited.add((i, j))
                        dfs(i, j)
            
            return islands
        
        if count_islands() != 1:
            return 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # Still one island after removing one land cell
                    grid[i][j] = 0
                    if count_islands() != 1:
                        # Disconnected after removing one land cell
                        return 1
                    grid[i][j] = 1
        
        return 2