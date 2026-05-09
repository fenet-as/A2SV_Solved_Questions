class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        

        row = len(grid)
        cols = len(grid[0])

        dir = [ (0,1),(1,0),(-1,0),(0,-1)]

        def inbound(i,j):
            return 0 <= i < row and 0 <= j < cols

        q = deque()
        visited = set()

        if all( grid[i][j] == 1 for i in range(row) for j in range(cols)):
            return -1
            
        if all( grid[i][j] == 0 for i in range(row) for j in range(cols)):
            return -1



        for i in range(row):
            for j in range(cols):
                if grid[i][j] == 1:
                    q.append((i,j))
                    visited.add((i,j))
            
        def calc(r,c,nr,nc):
            return abs(nr-r) + abs(nc-c)


        max_dist = 0
        while q:

            for _ in range(len(q)):
                r,c = q.popleft()

                for x,y in dir:
                    nr,nc = r+x , c+y

                    if inbound(nr,nc) and (nr,nc) not in visited:
                        
                        q.append((nr,nc))
                        visited.add((nr,nc))
            max_dist += 1

        return max_dist-1


