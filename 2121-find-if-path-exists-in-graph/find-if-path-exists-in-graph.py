class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:

        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        vis = set()
        def dfs(curr, vis):
            vis.add(curr)
            if curr == destination: return True

            for e in adj[curr]:
                if e not in vis:
                    if dfs(e,vis):return True

            return False
                




        return dfs(source,vis)

        