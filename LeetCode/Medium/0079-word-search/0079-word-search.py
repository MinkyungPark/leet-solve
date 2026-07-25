class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(x, y, i):
            if board[x][y] != word[i]:
                return False

            if i == len(word) - 1:
                return True
            
            origin = board[x][y]
            board[x][y] = 0
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                
                if dfs(nx, ny, i + 1):
                    board[x][y] = origin
                    return True
        
            board[x][y] = origin
            return False


        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False