class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()

        dir = [(0,1),(1,0),(-1,0),(0,-1)]

        def in_bound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1"

        def dfs(i,j):

            visited.add((i,j))

            for x,y in dir:
                nr,nc = i + x,j + y

                if in_bound(nr,nc) and (nr,nc) not in visited:
                    dfs(nr,nc)

        islands = 0    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    islands += 1
        return islands
                
                
