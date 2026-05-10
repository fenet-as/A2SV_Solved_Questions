class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dir = [(1,0),(0,1),(-1,0),(0,-1)]

        row = len(image)
        cols = len(image[0])

        def inbound(i,j):
            return 0 <= i < row and 0 <= j < cols

        
        q = deque([(sr,sc)])
        visited = set([(sr,sc)])
        org = image[sr][sc]
        image[sr][sc] = color

        while q:
            r,c = q.popleft()

            for x,y in dir:
                nr,nc = r+x,c+y

                if inbound(nr,nc) and ((nr,nc)) not in visited and  image[nr][nc] == org:
                    image[nr][nc] = color
                    q.append((nr,nc))
                    visited.add((nr,nc))
        
        return image

        
