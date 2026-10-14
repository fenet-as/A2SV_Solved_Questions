class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        

        for i in range(len(grid1)):
            for j in range(len(grid1[0])):

                if grid2[i][j] == 1 and grid1[i][j] == 0 :
                    grid1[i][j] = -1

                elif grid2[i][j] == 0:
                    grid1[i][j] = 0

        def inbound(i,j):
            return 0 <= i < len(grid1) and 0 <= j < len(grid1[0])

        
        count = 0
        visited = set()

        dir = [(0,1),(1,0),(-1,0),(0,-1)]

 

        def dfs(node):
            nonlocal valid
            visited.add(node)

            if grid1[node[0]][node[1]] == -1:valid = False


            for x,y in dir:
                nx = node[0] + x
                ny = node[1] + y

            

                if inbound(nx,ny) and (nx,ny) not in visited and grid1[nx][ny] != 0:
                    if  grid1[nx][ny] == -1:valid = False
                    dfs((nx,ny))

                

         

        

        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j] != 0 and (i,j) not in visited:
                    valid = True
                    dfs((i,j))
                    if valid: count +=1 
        return count   








                
