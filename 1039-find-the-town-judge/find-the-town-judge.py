class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for u,v in trust:
            outdegree[u] += 1
            indegree[v] += 1

        for i in range(1,n+1):
            if indegree[i] == n-1 and not outdegree[i]:return i
        return -1
        
