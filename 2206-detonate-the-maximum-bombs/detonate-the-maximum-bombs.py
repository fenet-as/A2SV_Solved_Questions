# d < r1+r2 --- 2 cicles overlap if the ditance between their centers is less that their radius rnages
# circle have equal radius length on every point

import math
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        

        graph = defaultdict(list)


        for i in range(len(bombs)):
            x,y,r = bombs[i]
            for j in range(len(bombs)):
                if i == j :
                    continue
                nx,ny,nr = bombs[j]
                dist = pow((x-nx),2) + pow((y-ny),2)
                if dist <= pow(r,2):
                    graph[i].append(j)
                


    
        # print(graph)
        # ans = 1
        def dfs(node,visited):

            visited.add(node)
            ans = 1

            for nei in graph[node]:
                if nei not in visited:
                    ans += dfs(nei,visited)
            return ans

        mx = 1 
        for i in range(len(bombs)):
            ans = dfs(i,set())
            mx = max(ans,mx)
          

        return mx