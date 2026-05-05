class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dir = [(0,1),(1,0),(-1,0),(0,-1)]

        row, col = len(grid),len(grid[0])

        def inbound(i,j):
            return 0 <= i < row and 0 <= j < col


        fresh = 0
        q = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        minutes = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                for x,y in dir:
                    nr,nc = r + x,c+y

                    if inbound(nr,nc):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr,nc))
                            fresh -= 1

            minutes += 1
        
        if fresh > 0:
            return -1
        return max(minutes-1,0)

        