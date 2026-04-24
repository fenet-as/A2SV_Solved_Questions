class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(starts):
            visited = set()
            stack = list(starts)

            while stack:
                r, c = stack.pop()
                if (r, c) in visited:
                    continue
                visited.add((r, c))

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n and
                        heights[nr][nc] >= heights[r][c]):
                        stack.append((nr, nc))

            return visited

        pacific_starts = [(0,j) for j in range(n)] + [(i,0) for i in range(m)]
        atlantic_starts = [(m-1,j) for j in range(n)] + [(i,n-1) for i in range(m)]

        pac = bfs(pacific_starts)
        atl = bfs(atlantic_starts)

        return list(pac & atl)