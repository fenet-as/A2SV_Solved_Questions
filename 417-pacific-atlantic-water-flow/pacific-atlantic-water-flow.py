class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        dir = [[0,1],[1,0],[-1,0],[0,-1]]



        def inbound(i,j):
            return 0 <= i < len(heights) and 0 <= j < len(heights[0])

        state = {(i,j):[0,0] for i in range(len(heights)) for j in range(len(heights[0]))}

        visited = [set(),set()]


        def dfs(i,j,t):

            if (i,j) in visited[t]:
                return
            visited[t].add((i,j))
            state[(i,j)][t] = 1                

            for x,y in dir:
                nr,nc = i+x, j+y

                if inbound(nr,nc) and (nr,nc) not in visited[t]:
                    if heights[nr][nc] >= heights[i][j]:
                        dfs(nr,nc,t)
                
                

            
        # left - pac
        for i in range(len(heights)):
            dfs(i,0,1)
        

        # right - atl
        for i in range(len(heights)):
            dfs(i,len(heights[0])-1,0)
        

        # top - pac
        for j in range(len(heights[0])):
            dfs(0,j,1)
        # buttom - atla
        for j in range(len(heights[0])):
            dfs(len(heights)-1,j,0)            
                

        res = [list(e) for e in state if state[e] == [1,1] ]

        return res


         
                  

                




