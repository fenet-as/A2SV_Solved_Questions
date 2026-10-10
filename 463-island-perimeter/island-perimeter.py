class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        

        def inbound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        visited = set()

        count = 0

        def dfs(i,j):

            nonlocal count

            visited.add((i,j))

     
            for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx = i+x
                ny = j+y

                if not inbound(nx,ny): count += 1
                else:
                    if grid[nx][ny] == 0: count += 1
                    elif (nx,ny) not in visited:
                            dfs(nx,ny)


        found = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i,j)
                    found = True
                    break
            if found: break
                
        return count

        
