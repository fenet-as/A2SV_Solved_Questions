class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # 🔹 Optimization 1: prune by character count
        from collections import Counter
        if Counter(word) - Counter(c for row in board for c in row):
            return False

        # 🔹 Optimization 2: reverse word if helpful
        if word.count(word[0]) > word.count(word[-1]):
            word = word[::-1]

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False
            
            if board[r][c] != word[i]:
                return False

            # mark visited
            temp = board[r][c]
            board[r][c] = "#"

            # explore 4 directions
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                if dfs(r + dr, c + dc, i + 1):
                    return True

            # backtrack
            board[r][c] = temp
            return False

        # try every starting cell
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False