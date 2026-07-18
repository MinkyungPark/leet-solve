from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def bfs(x, y):
            q = deque([(x, y)])

            while q:
                x, y = q.popleft()

                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < n and 0 <= ny < m
                        and grid[nx][ny] == "1"
                    ):
                        grid[nx][ny] = "0"
                        q.append((nx, ny))
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "0":
                    continue

                bfs(i, j)
                ans += 1

        return ans