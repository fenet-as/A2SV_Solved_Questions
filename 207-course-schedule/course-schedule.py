class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:



        adj = defaultdict(list)

        for u,v in prerequisites:
            adj[u].append(v)

        white = 1
        grey = 2
        black = 3

        colors = { k : white for k in range(numCourses)}

    
        def dfs(node):
            colors[node] = grey
        
            for nei in adj[node]:
                if colors[nei] == white:
                    if dfs(nei):
                        return True
                elif colors[nei] == grey:
                    return True

            colors[node] = black
            return False

        for n in range(numCourses):
            if colors[n] == white:
                if dfs(n):
                    return False

        return True





