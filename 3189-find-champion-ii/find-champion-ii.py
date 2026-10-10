class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        indegree = defaultdict(int)
        outdegree = defaultdict(int)


        for u,v in edges:
            outdegree[u] += 1
            indegree[v] += 1


        champs = []
        for i in range(n):
            if not indegree[i]: champs.append(i)

        if len(champs) == 1:
            return champs[0]
        return -1

