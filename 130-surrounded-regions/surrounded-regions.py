class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
     

        dir = [(1,0),(0,1),(-1,0),(0,-1)]
        def inbound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])


        def dfs(i,j):
            grid[i][j] = "#"

            for x,y in dir:
                nr,nc = i + x,j + y

                if inbound(nr,nc) and grid[nr][nc] == "O":
                    dfs(nr,nc)
              

        last_row = len(grid)-1
        last_col = len(grid[0])-1

        for i in range(len(grid)):
            if grid[i][0] == "O":
                dfs(i,0)

        for j in range(len(grid[0])):
            if grid[0][j] == "O":
                dfs(0,j)

        for j in range(len(grid[0])):
            if grid[last_row][j] == "O":
                dfs(last_row,j)
        
        for i in range(len(grid)):
            if grid[i][last_col] == "O":
                dfs(i,last_col)
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "#":
                    grid[i][j] = "O"

                elif grid[i][j] == "O":
                    grid[i][j] = "X"

                




        
        
    