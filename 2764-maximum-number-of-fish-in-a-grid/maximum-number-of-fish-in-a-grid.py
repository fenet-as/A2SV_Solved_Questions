class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        def inbound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])


        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        maximum = 0

        def dfs(i,j,visited):
            summ = grid[i][j]
            visited.add((i,j))

            for x,y in dir:
                nx = i+x
                ny = j+y

                if inbound(nx,ny) and (nx,ny) not in visited and grid[nx][ny] > 0:
                    summ += dfs(nx,ny,visited)


            return summ


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    maximum = max(maximum, dfs(i,j,set()))

        return maximum
            



