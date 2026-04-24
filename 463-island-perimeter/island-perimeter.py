class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direct = [[0,1] , [1,0], [0,-1] , [-1,0]]
        visited = set()
        ans = 0
        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1

        def dfs(row , col):
            nonlocal ans
            visited.add((row,col))
            
            for x , y in direct:
                newr , newc = row + x , col + y
                if not inbound(newr,newc) :
                    ans += 1
                elif (newr,newc) not in visited :
                    dfs(newr,newc)
                    
                   
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    visited.add((i , j))

                    dfs(i , j)
        return ans

        