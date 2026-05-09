class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        

        dir = [(1,0),(0,1),(-1,0),(0,-1)]

        row = len(mat)
        cols = len(mat[0])

        def inbound(i,j):
            return 0 <= i < row and 0 <= j < cols

        q = deque()
        move = 0
        visited = set()


        res = [[0]*cols for _ in range(row)]
        for i in range(row):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
                
                
        
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()


                for x,y in dir:
                    nr,nc = r+x,c+y
                    if inbound(nr,nc) and (nr,nc) not in visited:
                        res[nr][nc] = res[r][c] + 1
                        visited.add((nr,nc))
                        q.append((nr,nc))
            move += 1
        

        
        return res





                