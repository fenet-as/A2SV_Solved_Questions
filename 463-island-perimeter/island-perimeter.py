class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        

        def valid(pos):
            i,j = pos[0],pos[1]
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        visited = set()

        ct = [0]

        def dfs(pos):
            visited.add(pos)
            i,j = pos[0],pos[1]
            for dir in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx = i+dir[0]
                ny = j+ dir[1]

                if not valid((nx,ny)):ct[0]+=1
                else:

                    if (nx,ny) not in visited:
                        if grid[nx][ny] == 1:
                            dfs((nx,ny))
                        else: ct[0] += 1
                











        found = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs((i,j))
                    found = True
                    break
            if found: break
                    
        return ct[0]

        
