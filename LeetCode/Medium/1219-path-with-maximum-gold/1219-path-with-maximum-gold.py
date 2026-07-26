class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] == 0:
                return 0
            
            curr = grid[x][y]
            grid[x][y] = 0
            gold = curr

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                gold = max(gold, curr + dfs(nx, ny))
            
            grid[x][y] = curr
            return gold

        max_gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    max_gold = max(max_gold, dfs(i, j))
        
        return max_gold