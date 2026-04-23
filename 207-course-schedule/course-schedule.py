class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:



        adj = defaultdict(list)


        for u,v in prerequisites:
            adj[u].append(v)

        white = 1
        grey = 2
        black = 3

        colors = { k : white for k in range(numCourses)}

        cycle = False
        def dfs(node):
            nonlocal cycle
            if cycle:
                return

            colors[node] = grey
    
                
            for nei in adj[node]:
                
                if colors[nei] == black:
                    continue
                elif colors[nei] == grey:
                    cycle = True
                    return
                else:
                    dfs(nei)
                

            colors[node] = black

        for n in range(numCourses):
            if colors[n] == black:
                continue
            dfs(n)
        
        if not cycle:
            return True
        return False




