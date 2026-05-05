class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        dir = [(1,0),(0,1), (-1,0), (0,-1)]


        def inbound(i,j):
            return 0 <= i < row and 0 <= j < col

        visited = set()
        count = 0


        def dfs(i,j):
            nonlocal count

            visited.add((i,j))

            for x,y in dir:
                nr,nc = i+x,j+y

                if inbound(nr,nc):
                    if grid[nr][nc] == 0:
                        count += 1
                    elif (nr,nc) not in visited:
                        dfs(nr,nc)
                else:
                    count += 1

        

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visited:
                    dfs(i,j)


        return count


             