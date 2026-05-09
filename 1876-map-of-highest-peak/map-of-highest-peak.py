class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row = len(isWater)
        cols = len(isWater[0])

        dir = [(0,1),(1,0),(-1,0),(0,-1)]


        def inbound(i,j):
            return 0 <= i < row and 0 <= j < cols

        res = [[0]*cols for _ in range(row)]

        visited = set()
        q = deque()


        for i in range(row):
            for j in range(cols):
                if isWater[i][j] == 1:
                    visited.add((i,j))
                    q.append((i,j))

        while q:
            r,c = q.popleft()

            for x,y in dir:
                nr,nc = x+r,y+c

                if inbound(nr,nc) and (nr,nc) not in visited:
                    res[nr][nc] = res[r][c] + 1
                    visited.add((nr,nc))
                    q.append((nr,nc))

        return res

        
