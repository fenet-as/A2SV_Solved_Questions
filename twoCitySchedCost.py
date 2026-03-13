class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key = lambda x:x[0]-x[1])

        i = 0
        j = len(costs)-1
        sm = 0
        while i < j:
            f = costs[j][0] + costs[i][1]
            s = costs[i][0] + costs[j][1]


            sm += min(f,s)
            i += 1
            j -= 1
        return sm
