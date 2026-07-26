class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] == -1:
                return 0

            if grid[x][y] == 2:
                for i in range(m):
                    for j in range(n):
                        if grid[i][j] == 0:
                            return 0
                return 1
            
            origin = grid[x][y]
            grid[x][y] = -1
            cnt = 0 
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                cnt += dfs(nx, ny)

            grid[x][y] = origin
            return cnt

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += dfs(i, j)
        
        return ans
